import os 
import tkinter as tk # Importa a biblioteca que possibilitar criar interface grafica
from tkinter import filedialog, ttk, messagebox
import pandas as pd
from leitura.leitor_xml import LeitorXML # Chama o metodo LeitorXML la do arquivo leitor_XML
from tqdm import tqdm #  Barra de carregamento
from datetime import datetime

# Cria a classe Janela Principal
class JanelaPrincipal:

    # Inicializa a janela principal
    def __init__(self):
        self.janela = tk.Tk() #Cria a janela principal do programa
        self.janela.title("Leitor de XML 2.0") # Define o título da janela
        self.janela.minsize(1000, 700) # Define o tamanho mínimo da janela

        self.arquivos_notas = {}

        self.leitor = LeitorXML()

        # Define o Frame
        self.frame_cabecalho = tk.Frame( # Cria o Frame do cabeçalho
            self.janela, # O Frame pertence à janela principal
            bg="lightblue", # Define a cor de fundo do Frame
            height=80 # Define a altura do Frame
        )
        self.frame_cabecalho.pack(fill="x") # Faz o Frame ocupar toda a largura da janela

        # Cria um atributo chamado Label escrito bem vindo
        self.label_boas_vindas = tk.Label( # Cria o Frame do cabeçalho
            self.frame_cabecalho, # O Label pertence ao Frame do cabeçalho
            text="XXXXXXXXXXX", # Texto exibido na tela
            font=("Arial", 18, "bold") # Fonte Arial, tamanho 18 e em negrito
        )
        self.label_boas_vindas.pack(pady=20) # Exibe o Label e adiciona um espaçamento vertical

        self.frame_botoes = tk.Frame(self.janela) # Cria o Frame do botao importar XML

        self.frame_botoes.pack(pady=20) # Exibe o Label e adiciona um espaçamento vertical

        self.botao_importar = tk.Button( # Cria o botao
            self.frame_botoes, # Coloca o botao dentro do frame
            text="Importar XML", # Texto exibido dentro do botao
            font=("Arial"), # Fonte de dentro do botao
            command=self.importar_xml, # Comando que chama a funcao importar_xml
            width= 21, # Altura do botao
            height= 4 # Largura do botao
            
        )
        self.botao_importar.pack(side="left", padx=10) # Exibe o Label e adiciona um espaçamento vertical

        self.botao_limpar_tabela = tk.Button(
            self.frame_botoes, # Coloca o botao dentro do frame
            text="Limpar Tabela", # Texto exibido dentro do botao
            font=("Arial"), # Fonte de dentro do botao
            command=self.limpar_tabela, # Comando que chama a funcao limpar tabela
            width= 21, # Altura do botao
            height= 4 # Largura do botao
        )

        self.botao_limpar_tabela.pack(side="left", padx=10) # Exibe o Label e adiciona um espaçamento vertical

        self.botao_exportar_excel = tk.Button(
            self.frame_botoes, # Coloca o botao dentro do frame
            text="Exportar Excel", # Texto exibido dentro do botao
            font=("Arial"), # Fonte de dentro do botao
            command=self.exportar_excel, # Comando que chama a funcao limpar tabela
            width= 21, # Altura do botao
            height= 4 # Largura do botao
        )

        self.botao_exportar_excel.pack(side="left", padx=10) # Exibe o Label e adiciona um espaçamento vertical

        self.botao_exportar_pdf = tk.Button(
            self.frame_botoes, # Coloca o botao dentro do frame
            text="Importar PDF", # Texto exibido dentro do botao
            font=("Arial"), # Fonte de dentro do botao
            command=self.exportar_pdf, # Comando que chama a funcao limpar tabela
            width= 21, # Altura do botao
            height= 4 # Largura do botao
        )

        self.botao_exportar_pdf.pack(side="left", padx=10) # Exibe o Label e adiciona um espaçamento vertical


        self.informacoes_tabela = tk.Label( # Cria um label com informacoes relacionadas as informacoes do XML
            self.janela,
            text="XMLs Importados = 0      Valor Total = 0      Periodo de Emissao:",
            font=("Arial", 12)
            ) # Cria o Frame das informacoes da tabela

        self.informacoes_tabela.pack(pady=20) # Exibe o Label e adiciona um espaçamento vertical

        self.barra_progresso = ttk.Progressbar( # Cria uma barra de progresso
            self.janela,
            orient="horizontal",
            length=400,
            mode="determinate"
        )

        self.barra_progresso.pack(pady=20) #Exibe a barra de carregamento



        # Define as colunas que a tabela vai ter
        colunas = ("Tipo", 
                   "Numero", 
                   "Serie", 
                   "Data", 
                   "Emitente", 
                   "Valor", 
                   "Pagamento")

        # Cria o Treeview (a tabela) dentro da janela, usando as colunas definidas
        # O parâmetro show="headings" garante que só as colunas definidas apareçam,
        # removendo a coluna extra "#0" que o Treeview cria por padrão.
        self.tabela = ttk.Treeview (
            self.janela, 
            columns=colunas, 
            show="headings")

        # Define o título (cabeçalho) da coluna "Tipo"
        self.tabela.heading("Tipo", text="Tipo:")

        # Define o título da coluna "Numero"
        self.tabela.heading("Numero", text="Número da nota:")

        # Define o título da coluna "Serie"
        self.tabela.heading("Serie", text="Número de Serie:")

        # Define o título da coluna "Data"
        self.tabela.heading("Data", text="Data:")

        # Define o título da coluna "Emitente"
        self.tabela.heading("Emitente", text="Emitente:")

        # Define o título da coluna "Valor"
        self.tabela.heading("Valor", text="Valor:")

        # Define o título da coluna "Pagamento"
        self.tabela.heading("Pagamento", text="Forma de Pagamento:")

        self.tabela.bind("<<TreeviewSelect>>", self.selecionar_nota)

    
        
        # Exibe a tabela na janela
        self.tabela.pack()

        self.produtos_nota = ttk.Treeview(
            self.janela
        )

    def selecionar_nota(self, evento):
        notaSelecionada = self.tabela.selection()
        id_item = notaSelecionada[0]
        caminho_xml = self.arquivos_notas[id_item]
        produtos = self.leitor.buscar_produtos(caminho_xml)
        print(produtos)
        

    def importar_xml(self): # Cria a funcao importar_xml
        caminho = filedialog.askdirectory() # Abre o explorador de pastas

        if caminho: # Se a variavel caminho estiver preenchida escreve no console a pasta que abriu
            print(caminho) 
        else: # Se nao escreve no console que nenhuma pasta foi selecionada
            print("Nenhuma pasta foi selecionada.")

        quantidade_xml = 0 # Quantidade de XML

        arquivos = os.listdir(caminho) # Lista todos os arquivos da pasta selecionada
        
        quantidade_xml = 0 # Declara a quantidade de XML importados como zero

        valor_total = 0 # Valor total de dinheiro dos XMLs lidos

        total_arquivos = len(arquivos)

        menor_data = None # Variavel que armazena a menor data de emissao do xml

        maior_data = None # Variavel que armazena a maior data de emissao do xml

        arquivos_notas = {}

        for arquivo in arquivos: # Percorre cada arquivo da lista

            if arquivo.endswith(".xml"): # Se for encontrado um arquivo que for .xml ele escrevera o XML no console
                
                print(arquivo)
                caminho_arquivo = os.path.join(caminho, arquivo) # Junta o caminho da pasta com o nome do arquivo para obter o caminho completo do XML.

                dados = self.leitor.abrir_xml(caminho_arquivo) # Chama o método abrir_xml() para abrir e ler o arquivo XML.

                produtos = self.leitor.buscar_produtos(caminho_arquivo)

                print(produtos)

                data_atual = datetime.strptime(dados[3], "%d/%m/%Y %H:%M:%S")

                if menor_data is None:
                    menor_data = data_atual
                    maior_data = data_atual
                else:
                    if data_atual < menor_data:
                        menor_data = data_atual

                    if data_atual > maior_data:
                        maior_data=data_atual    

                valor_total += dados[5]

                id_item = self.tabela.insert("", "end", values=dados)
                self.arquivos_notas[id_item] = caminho_arquivo
                arquivos_notas[id_item] = caminho_arquivo

                quantidade_xml += 1 # acrescenta um no contador de XML
                progresso = (quantidade_xml / total_arquivos) * 100



            self.barra_progresso["value"] = progresso
            self.janela.update_idletasks()

        print("Menor data:", menor_data)
        print("Maior data:", maior_data)
        print(f"Foram encontrados {quantidade_xml} arquivos XML.") # Escreve no console a quantidade de XML lido.
        print(f"O valor total R$: {valor_total}") # Escreve no console o total

        # Atualiza as informacoes de quantidade xml lido.
        self.informacoes_tabela.config(
            text=f"XMLs importados: {quantidade_xml}      Valor Total R$: {valor_total:.2f}      Periodo de Emissao: {menor_data} até {maior_data}",
            )

    def limpar_tabela(self):
        resposta = messagebox.askyesno(
            "Confirmação",
            "Deseja realmente limpar a tabela?"
        )

        if resposta:  # Se o usuário clicar em "Sim"
            for item in self.tabela.get_children(): # Para cada item que esta na tabela
                self.tabela.delete(item)

            self.informacoes_tabela.config(
                text="XMLs Importados = 0      Valor Total = 0      Periodo de Emissao:"
            )

    def exportar_excel(self):
        messagebox.showwarning(
        "Botão Indisponível",
        "Este botão ainda não está disponível."
    )

    def exportar_pdf(self):
        messagebox.showwarning(
        "Botão Indisponível",
        "Este botão ainda não está disponível."
    )
        

    # Inicia a interface gráfica
    def executar(self):
        self.janela.mainloop()
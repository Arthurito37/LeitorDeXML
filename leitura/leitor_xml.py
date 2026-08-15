import xml.etree.ElementTree as ET # Importa a biblioteca responsável por ler e interpretar arquivos XML.
from datetime import datetime

# Classe responsável por abrir e ler os arquivos XML.
class LeitorXML:

    # Inicializa a classe LeitorXML.
    def __init__(self):
        pass # Ainda não há nenhuma inicialização necessária.

    def formatar_cnpj(self, doc):
        # Se tiver 11 dígitos → CPF
        if len(doc) == 11:
            return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}"
    
        #Se tiver 14 dígitos → CNPJ
        elif len(doc) == 14:
            return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}"
        else:
            return "Documento inválido"

    def formatar_data(self, data_iso):
        # Converte a string ISO para objeto datetime
        dt = datetime.fromisoformat(data_iso)
        # Formata no padrão brasileiro
        return dt.strftime("%d/%m/%Y %H:%M:%S")

    def formatar_dinheiro(self, cash):
        # cash já é string, então só troca o ponto pela vírgula
        return cash.replace(".", ",")


        
    # Abre um arquivo XML a partir do caminho informado.
    def abrir_xml(self, caminho_xml): 
        arvore = ET.parse(caminho_xml) # Lê o arquivo XML e cria uma árvore com todos os seus elementos.

        # Obtém a raiz da árvore (primeira tag do XML).
        raiz = arvore.getroot()
        # Define o namespace utilizado no XML da NF-e/NFC-e.
        namespace = {
            "nfe": "http://www.portalfiscal.inf.br/nfe"
        }

        # Procura a tag NFe dentro da raiz do XML.
        NFe = raiz.find("nfe:NFe", namespace)

        # Procura a tag infNFe dentro da tag NFe.
        infNFe = NFe.find("nfe:infNFe", namespace)

        # Procura a tag ide, que contém as informações de identificação da nota fiscal.
        ide = infNFe.find("nfe:ide", namespace)



        # Extrai o modelo do documento fiscal (55 = NF-e, 65 = NFC-e).
        modeloNota = ide.find("nfe:mod", namespace)

        # Exibe no terminal o modelo da nota fiscal.
        if modeloNota.text == "65":
            print("Tipo: NFCe")
            modeloNota = "NFCe"
        else:
            print("Tipo: NFe")
            modeloNota = "NFe"


        # Extrai a série da nota fiscal.
        numeroSerie = ide.find("nfe:serie", namespace)

        # Exibe no terminal a série da nota fiscal.
        print(f"Numero de serie da nota {numeroSerie.text}.")

        # Extrai o número da nota fiscal.
        numeroNota = ide.find("nfe:nNF", namespace)

        # Exibe no terminal o número da nota fiscal.
        print(f"O numero da nota e {numeroNota.text}.")

        # Extrai a data e hora de emissão da nota fiscal.
        dataEmissao = ide.find("nfe:dhEmi", namespace)

        # Exibe no terminal a data e hora de emissão.
        print(f"Data da emissao da nota {dataEmissao.text}.")
        dataEmissao = self.formatar_data(dataEmissao.text)

        # Procura a data e hora de saída/entrada da mercadoria (essa tag pode não existir).
        dataSaida = ide.find("nfe:dhSaiEnt", namespace)

        # Verifica se a tag dhSaiEnt foi encontrada antes de acessar seu conteúdo.
        if dataSaida is not None:
            print(f"Data de saida da nota {dataSaida.text}.")
            dataSaida = self.formatar_data(dataSaida.text)

# --------------------------------------- Emitente -----------------------------------------

        # Procura a tag emit que contem as informacoes do emitente
        emit = infNFe.find("nfe:emit", namespace)

        # Procura a tag emit que contem o numero do CNPJ
        numeroCNPJ = emit.find("nfe:CNPJ", namespace)

        # Exibe no terminal o CNPJ
        print(f"CNPJ: {numeroCNPJ.text}.")
        numeroCNPJ = self.formatar_cnpj(numeroCNPJ.text)

        # Procura a tag emit que contem a razao social
        razaoSocial = emit.find("nfe:xNome", namespace)

        # Exibe no terminal a razao social do emitente.
        print(f"Razão Social: {razaoSocial.text}.")

        # Extrai o nome fantasia do emitente.
        nomeFantasia = emit.find("nfe:xFant", namespace)

        # Se tiver nome fantasia
        if nomeFantasia is not None:
            print(f"Nome Fantasia: {nomeFantasia.text}.")

        # Extrai a inscrição estadual do emitente.
        inscricaoEstadual = emit.find("nfe:IE", namespace)

        # Exibe no terminal a IE do emitente
        print(f"Inscrição Estadual: {inscricaoEstadual.text}.")

        # Procura a tag enderEmit onde tem o endereco do emitente
        enderEmit = emit.find ("nfe:enderEmit", namespace)

        # Extrai o logradouro do emitente.
        logradouro = enderEmit.find("nfe:xLgr", namespace)

        # Exibe no terminal o logradouro
        print(f"Logradouro: {logradouro.text}.")

        # Extrai o numero do endereco do emitente.
        numeroEndereco = enderEmit.find("nfe:nro", namespace)

        # Exibe no terminal o numero do endereco
        print(f"Numero: {numeroEndereco.text}.")

        # Extrai o bairro do emitente.
        bairro = enderEmit.find("nfe:xBairro", namespace)

        # Exibe no terminal o bairro
        print(f"Bairro {bairro.text}.")

        # Extrai o municipio do emitente.
        municipio = enderEmit.find("nfe:xMun", namespace)

        # Exibe no terminal o municipio
        print(f"Municipio {municipio.text}.")

        # Extrai o uf do emitente.
        uf = enderEmit.find("nfe:UF", namespace)

        # Exibe no terminal o UF
        print(f"UF: {uf.text}.")

        # Extrai o cep do emitente.
        cep = enderEmit.find("nfe:CEP", namespace)

        # Exibe no terminal o CEP
        print(f"CEP: {cep.text}.")

# --------------------------------------- Destinatario -----------------------------------------
        # Procura o destinatario
        dest = infNFe.find("nfe:dest", namespace)

        # Se o destinatario estiver
        if dest is not None:

            #Procura o campo CPF ou CNPJ
            numeroCPF = dest.find("nfe:CPF", namespace)

            # Se tiver o CPF:
            if numeroCPF is not None:

                #Escreve o CPF
                print(f"CPF: {numeroCPF.text}")
                numeroCPF = self.formatar_cnpj(numeroCPF.text)

            # Procura o campo nome:
            nomeDestinatario = dest.find("nfe:xNome", namespace)

            # Se tiver o nome
            if nomeDestinatario is not None:

                # Escreve o nome:
                print(f"Nome: {nomeDestinatario.text}")

# --------------------------------------- Impostos -----------------------------------------

        # Procura o total
        total = infNFe.find("nfe:total", namespace)

        # Procura no ICMStot
        ICMSTot = total.find("nfe:ICMSTot", namespace)

        # Procura o valor do produtos
        valorProdutos = ICMSTot.find("nfe:vProd", namespace)

        # Escreve o valor dos produtos
        print(f"Valor dos Produtos: {valorProdutos.text}")
        valorProdutos = self.formatar_dinheiro(valorProdutos.text)

        # Procura o valor da nota
        valorNota = ICMSTot.find("nfe:vNF", namespace)

        # Escreve o valor da nota
        print(f"Valor da Nota: {valorNota.text}")
        valorNota = float(valorNota.text)

        # Procura o valor do desconto
        valorDesconto = ICMSTot.find("nfe:vDesc", namespace)
        

        # Escreve o valor do desconto
        print(f"Valor do Desconto: {valorDesconto.text}")
        valorDesconto = self.formatar_dinheiro(valorDesconto.text)

        # Procura o valor do frete
        valorFrete = ICMSTot.find("nfe:vFrete", namespace)
        

        # Escreve o valor do frete
        print(f"Valor do Frete: {valorFrete.text}")
        valorFrete = self.formatar_dinheiro(valorFrete.text)

        # Procura o ICMS
        valorICMS = ICMSTot.find("nfe:vICMS", namespace)
        

        # Escreve o nome:
        print(f"Valor do ICMS: {valorICMS.text}")
        valorICMS = self.formatar_dinheiro(valorICMS.text)

        # Procura o valor do IP
        valorIPI = ICMSTot.find("nfe:vIPI", namespace)

        # Se o IP estiver
        if valorIPI is not None:
            print(f"Valor do IPI: {valorIPI.text}")

# --------------------------------------- Pagamento -----------------------------------------
        # Procura a tag pag
        pag = infNFe.find("nfe:pag", namespace)

        # Procura a tag detPag
        detPag = pag.find("nfe:detPag", namespace)

        # Procura o numero da forma de pagamento
        formaPagamento = detPag.find("nfe:tPag", namespace)

        # Faz o tratamento dos valores 
        if formaPagamento.text == "01":

            # Escreve a forma de pagamento
            print("Forma de pagamento: Dinheiro")
            formaPagamento = "DINHEIRO"

        elif formaPagamento.text == "03":
            # Escreve a forma de pagamento
            print("Forma de pagamento: Cartao de Credito")
            formaPagamento = "CARTAO DE CREDITO"

        elif formaPagamento.text == "04":
            # Escreve a forma de pagamento
            print("Forma de pagamento: Cartao de Debito")
            formaPagamento = "CARTAO DE DEBITO"
        elif formaPagamento.text == "17":

            # Escreve a forma de pagamento
            print("Forma de pagamento: PIX")
            formaPagamento = "PIX"

        elif formaPagamento.text == "99":
            # Escreve a forma de pagamento
            print("Forma de pagamento: Outros")
            formaPagamento = "OUTROS"

        else:
            print("Forma de pagamento nao encontrada")

        # Procura o valor pago
        valorPago = detPag.find("nfe:vPag", namespace)

        #Escreve o valor pago
        print(f"O valor pago: {valorPago.text}")
        valorPago = self.formatar_dinheiro(valorPago.text)

        # Procura o valor do troco.
        valorTroco = pag.find("nfe:vTroco", namespace)

        # Verifica se existe troco.
        if valorTroco is not None:
            print(f"Troco: {valorTroco.text}")

# --------------------------------------- Produtos -----------------------------------------
        # Procura a lista de produtos na tag det
        produtos = infNFe.findall("nfe:det", namespace)

        # Para cada produto encontrado
        for produto in produtos: 

            # Procura os produtos na tag prod
            prod = produto.find("nfe:prod", namespace)

            # Procura o codigo do produto
            codigo = prod.find("nfe:cProd", namespace)

            # Escreve o codigo do produto
            print(f"Código: {codigo.text}")

            # Procura a descricao do produto
            descricao = prod.find("nfe:xProd", namespace)

            # Escreve a descricao do produto
            print(f"Descrição: {descricao.text}")

            # Procura o NCM do produto
            ncm = prod.find("nfe:NCM", namespace)

            # Escreve o NCM do produto
            print(f"NCM: {ncm.text}")

            # Procura o CFOP do produto
            cfop = prod.find("nfe:CFOP", namespace)

            # Escreve o CFOP do produto
            print(f"CFOP: {cfop.text}")

            # Procura a unidade 
            unidade = prod.find("nfe:uCom", namespace)

            #Escreve a unidade
            print(f"Unidade: {unidade.text}")

            # Procura a quantidade do produto
            quantidade = prod.find("nfe:qCom", namespace)

            # Escreve a quantidade do produto
            print(f"Quantidade: {quantidade.text}")

            # Procura o valor do produto
            valorUnitario = prod.find("nfe:vUnCom", namespace)

            # Escreve o valor do produto 
            print(f"Valor Unitário: {valorUnitario.text}")

            # Procura o valor do total quantidade vezes valor do produto
            valorProduto = prod.find("nfe:vProd", namespace)

            # Escreve o valor total
            print(f"Valor Total: {valorProduto.text}")

            # Escreve quarenta -
            print("-" * 40)

# --------------------------------------- Identificacao -----------------------------------------

        # Procura a tag infNFe dentro da tag NFe.
        chaveNota = infNFe.get("Id")
        print(f"Chave da nota:{chaveNota}")

        # Procura a tag NFe dentro da raiz do XML.
        protNFe = raiz.find("nfe:protNFe", namespace)

        # Procura a tag protocolos
        infProt = protNFe.find("nfe:infProt", namespace)

        # Procura o Protocolo de autorizacao da nota
        protocoloNota = infProt.find("nfe:nProt", namespace)

        # Escreve o protocolocad anota
        print(f"Procolo da nota: {protocoloNota.text}")

        # Procura a autorizacao da nota
        dataAutorizacao = infProt.find("nfe:dhRecbto", namespace)

        # Escreve a nota
        print(f"Horario de Autorizacao:{dataAutorizacao.text}")
        dataAutorizacao = self.formatar_data(dataAutorizacao.text)

        return (
            # Indica se a nota corresponde a NFCe ou NFe
            modeloNota,
            # Numero da Nota
            numeroNota.text,
            #Numero de Serie
            numeroSerie.text,
            # Data de Emissao do XML
            dataEmissao,
            # Numero do XML
            numeroCNPJ,
            # Valor total da nota
            valorNota,
            # Forma de pagamento
            formaPagamento
        )

    def buscar_produtos(self, caminho_xml):

        arvore = ET.parse(caminho_xml) # Lê o arquivo XML e cria uma árvore com todos os seus elementos.

        # Obtém a raiz da árvore (primeira tag do XML).
        raiz = arvore.getroot()
        # Define o namespace utilizado no XML da NF-e/NFC-e.
        namespace = {
            "nfe": "http://www.portalfiscal.inf.br/nfe"
        }

        # Procura a tag NFe dentro da raiz do XML.
        NFe = raiz.find("nfe:NFe", namespace)

        # Procura a tag infNFe dentro da tag NFe.
        infNFe = NFe.find("nfe:infNFe", namespace)

        # Procura a tag ide, que contém as informações de identificação da nota fiscal.
        ide = infNFe.find("nfe:ide", namespace)

        # Procura a lista de produtos na tag det
        produtos = infNFe.findall("nfe:det", namespace)


        produtos_dados = []

            # Para cada produto encontrado
        for produto in produtos: 

            # Procura os produtos na tag prod
            prod = produto.find("nfe:prod", namespace)

            # Procura o codigo do produto
            codigo = prod.find("nfe:cProd", namespace)


            # Procura a descricao do produto
            descricao = prod.find("nfe:xProd", namespace)


            # Procura o NCM do produto
            ncm = prod.find("nfe:NCM", namespace)


            # Procura o CFOP do produto
            cfop = prod.find("nfe:CFOP", namespace)


            # Procura a unidade 
            unidade = prod.find("nfe:uCom", namespace)


            # Procura a quantidade do produto
            quantidade = prod.find("nfe:qCom", namespace)


            # Procura o valor do produto
            valorUnitario = prod.find("nfe:vUnCom", namespace)


            # Procura o valor do total quantidade vezes valor do produto
            valorProduto = prod.find("nfe:vProd", namespace)


        dados_produto = (
            codigo.text,
            descricao.text,
            ncm.text,
            cfop.text,
            unidade.text,
            quantidade.text,
            valorUnitario.text,
            valorProduto.text
        )

        produtos_dados.append(dados_produto)

        return produtos_dados





        


            








        


        
        



        

 







        
        
        
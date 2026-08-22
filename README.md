# 📄 LeitorDeXML 2.0

Aplicação desktop desenvolvida em **Python** para leitura, processamento e organização de dados provenientes de arquivos XML de documentos fiscais eletrônicos.

O projeto foi desenvolvido com o objetivo de automatizar a leitura de arquivos **NF-e (modelo 55)** e **NFC-e (modelo 65)**, permitindo extrair informações importantes dos documentos e gerar relatórios de forma rápida e organizada.

---

## 🚀 Funcionalidades

* 📂 Seleção de uma pasta contendo arquivos XML
* 🔎 Identificação automática dos arquivos XML
* 📄 Leitura de documentos **NF-e** e **NFC-e**
* 🧾 Extração de informações fiscais
* 🏢 Identificação dos dados do emitente
* 👤 Identificação dos dados do destinatário
* 💰 Extração de valores dos documentos
* 📅 Identificação da data de emissão
* 🔢 Identificação de número e série da nota
* 📊 Processamento dos dados encontrados
* ➕ Soma dos valores dos documentos
* 📑 Geração de relatórios
* 💾 Exportação dos resultados para arquivos
* 🖥️ Interface gráfica desenvolvida com Tkinter

---

## 📋 Informações extraídas

Entre os principais dados processados pelo sistema estão:

### Documento fiscal

* Modelo
* Número da nota
* Série
* Data de emissão
* Valor total
* Tipo de documento

### Emitente

* CNPJ
* Razão social
* Nome fantasia
* Inscrição estadual

### Destinatário

* CPF/CNPJ
* Nome
* Outras informações disponíveis no XML

O projeto também está sendo desenvolvido para ampliar a extração de informações relacionadas à **tributação e ICMS**.

---

## 🧾 Documentos suportados

Atualmente o sistema trabalha com os principais modelos de documentos fiscais eletrônicos:

| Modelo | Documento |
| ------ | --------- |
| 55     | NF-e      |
| 65     | NFC-e     |

O sistema identifica o modelo diretamente através da estrutura do XML.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Tkinter** — Interface gráfica
* **ElementTree** — Leitura e processamento dos XMLs
* **Pandas** — Organização e manipulação dos dados
* **OpenPyXL** — Geração de planilhas Excel
* **ReportLab** — Geração de relatórios PDF
* **OS** — Manipulação de arquivos e diretórios
* **Git/GitHub** — Versionamento do projeto

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/Arthurito37/LeitorDeXML.git
```

Entre na pasta do projeto:

```bash
cd LeitorDeXML
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o projeto

Execute o arquivo principal:

```bash
python main.py
```

Após iniciar a aplicação:

1. Clique em **Importar XML**.
2. Selecione a pasta que contém os arquivos XML.
3. O sistema realizará a leitura dos documentos.
4. Os dados serão processados e organizados.
5. Os relatórios poderão ser gerados conforme as funcionalidades disponíveis.

---

## 📁 Estrutura do projeto

Uma estrutura aproximada do projeto:

```text
LeitorDeXML/
│
├── main.py
├── leitor_xml.py
├── requirements.txt
├── README.md
│
├── relatorios/
│
└── arquivos/
```

A estrutura pode sofrer alterações conforme o desenvolvimento do projeto.

---

## 📊 Relatórios

O projeto possui recursos para geração de relatórios a partir dos XMLs processados.

Entre os formatos trabalhados estão:

* `.txt`
* `.xlsx`
* `.pdf`

Os relatórios permitem organizar as informações extraídas dos documentos fiscais e facilitar a conferência dos dados.

---

## 🧠 Objetivo do projeto

O **LeitorDeXML 2.0** foi criado como um projeto prático para aplicar conceitos de programação, automação e processamento de dados em uma situação real.

Além de facilitar o trabalho com documentos fiscais, o projeto tem como objetivo desenvolver conhecimentos em:

* Programação Python
* Orientação a objetos
* Manipulação de arquivos
* Processamento de XML
* Estruturas de dados
* Tratamento de exceções
* Interfaces gráficas
* Manipulação de dados
* Geração de relatórios
* Organização de projetos
* Versionamento com Git

---

## 🔄 Próximas melhorias

O projeto continua em desenvolvimento.

Algumas funcionalidades planejadas:

* [X] Extração completa dos campos principais da NF-e/NFC-e
* [X] Processamento dos produtos
* [X] Extração dos valores dos itens
* [ ] Processamento de impostos
* [ ] Leitura e organização do ICMS
* [ ] Processamento de outros tributos
* [ ] Melhorias na interface gráfica
* [ ] Filtros por período
* [ ] Filtros por emitente
* [ ] Dashboard com informações das notas
* [ ] Melhor tratamento de erros
* [ ] Melhor organização dos relatórios
* [ ] Empacotamento da aplicação para Windows

---

## 📌 Status do projeto

🟡 **Em desenvolvimento**

O projeto está sendo desenvolvido de forma incremental, adicionando novas funcionalidades conforme a evolução da aplicação.

---

## 👨‍💻 Autor

**Arthur de Sousa Santana**

Projeto desenvolvido para estudo, prática de programação e construção de portfólio na área de tecnologia.

---

## 📜 Licença

Este projeto é destinado a fins educacionais e de portfólio.


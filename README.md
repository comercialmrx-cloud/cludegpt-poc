# CludeGPT POC

## Trabalho Individual – MLOps

MBA em Inteligência Artificial e Analytics Aplicadas a Negócios – FGV

Autor: Marcos Colussi Carneiro

## Objetivo

Esta POC apresenta uma versão simplificada do CludeGPT, assistente proposto no trabalho individual da disciplina de MLOps.

A ideia é utilizar documentos da Clude Saúde para responder perguntas frequentes de usuários e empresas clientes.

## Arquitetura

Documentos

→ Chunking

→ Embeddings

→ FAISS

→ OpenAI

→ Resposta ao usuário

## Tecnologias Utilizadas

* Python
* Streamlit
* LangChain
* FAISS
* OpenAI API

## Estrutura do Projeto

```text
cludegpt-poc/
│
├── README.md
├── app.py
├── requirements.txt
└── docs/
    └── faq_clude.txt
```
## Como Executar

A aplicação foi estruturada para execução local em ambiente Python.

Dependências:

pip install -r requirements.txt

A aplicação foi estruturada para execução local em ambiente Python utilizando Streamlit.

```

## Exemplo de Pergunta

Como funciona o atendimento psicológico da Clude?

## Resultado Esperado

A solução foi estruturada para consultar documentos corporativos e utilizar essas informações na construção das respostas apresentadas ao usuário.

## Possíveis Evoluções

* Utilização de pgvector
* Registro de versões no MLflow
* Monitoramento com Langfuse
* Integração com documentos corporativos adicionais

## Relação com o Trabalho

Esta POC está relacionada à iniciativa CludeGPT apresentada no plano de evolução da Plataforma Digital de Saúde da Clude.

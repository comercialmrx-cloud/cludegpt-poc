import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="CludeGPT POC", page_icon="🩺")

st.title("CludeGPT – POC")
st.caption("Assistente inteligente baseado em RAG para documentos da Clude Saúde")

api_key = st.text_input("OpenAI API Key", type="password")
question = st.text_input("Digite sua pergunta:")

if api_key and question:
    os.environ["OPENAI_API_KEY"] = api_key

    loader = TextLoader("docs/faq_clude.txt", encoding="utf-8")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    docs = vectorstore.similarity_search(question, k=2)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    Responda com base apenas no contexto abaixo.

    Contexto:
    {context}

    Pergunta:
    {question}

    Resposta:
    """

    response = llm.invoke(prompt)

    st.subheader("Resposta")
    st.write(response.content)

    st.subheader("Fonte utilizada")
    st.write(context)

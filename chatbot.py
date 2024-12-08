import os
from dotenv import load_dotenv
from info import chroma_client, collection 
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# Configurar OpenAI Embeddings
load_dotenv()
openai_api_key = os.getenv("APIKEY")

# Crear embeddings

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Configurar el vectorstore con embeddings
vectorstore = Chroma(
    collection_name=collection.name,
    client=chroma_client,
    embedding_function=embeddings,  # Pasar el objeto embeddings directamente
)

# Configurar el sistema de QA
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key),
    retriever=retriever,
)

# Hacer una consulta
def responseFromBot(msg:str):
    query = msg
    response = qa_chain.run(query)
    return response

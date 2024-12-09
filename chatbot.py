import os
from dotenv import load_dotenv
from info import chroma_client, collection 
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Cargar la clave de la API
load_dotenv()
openai_api_key = os.getenv("APIKEY")

# Crear embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Configurar el vectorstore con embeddings
vectorstore = Chroma(
    collection_name=collection.name,
    client=chroma_client,
    embedding_function=embeddings,
)

# Definir el prompt personalizado
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "Eres un profesional de la salud mental. Responde todas las preguntas como si "
        "fueran de pacientes, basándote exclusivamente en la información proporcionada "
        "en el siguiente contexto: {context}\n\nPregunta: {question}\n\nRespuesta:"
    )
)

# Configurar el sistema de QA
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key),
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
)

# Función para consultar al bot
def responseFromBot(msg: str):
    query = msg
    response = qa_chain.run(query)
    return response

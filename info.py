import chromadb
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pdfFile

load_dotenv()
openai_api_key = os.getenv("APIKEY")

# Configurar cliente ChromaDB
chroma_client = chromadb.Client()

# Crear función de embeddings personalizada
class CustomEmbeddingFunction:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def __call__(self, input):
        if isinstance(input, list):
            return [self.embedding_model.embed_query(text) for text in input]
        return self.embedding_model.embed_query(input)

# Configurar embeddings de OpenAI
embeddings = CustomEmbeddingFunction(
    OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)
)

# Crear colección con la dimensión correcta
collection = chroma_client.create_collection(
    name="my_collection",
    embedding_function=embeddings,
    metadata={"embedding_dim": 1536}  # Especificar la dimensión correcta
)

# Simular texto para agregar
texto = "este es un documento para concientizar sobre mental health y todos sus aspectos relacionados, recomendaciones, estudios"#pdfFile.extraer_texto_pdf("mentalHealth.pdf")
fragmentos = [texto[i:i + 500] for i in range(0, len(texto), 500)]  # Fragmentos de 500 caracteres

# Agregar contenido extraído a la colección
for i, fragmento in enumerate(fragmentos):
    collection.add(
        documents=[fragmento],
        ids=[f"fragmento_{i + 1}"]
    )

# Inspeccionar contenido
contenido = collection.get()
print("Contenido de la colección:", contenido)
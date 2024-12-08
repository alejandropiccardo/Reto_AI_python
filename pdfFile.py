
import fitz  # PyMuPDF para manejar PDFs
import chromadb


# Extraer texto de un archivo PDF
def extraer_texto_pdf(archivo):
    texto = ''
    with fitz.open(archivo) as pdf_documento:
        for pagina in pdf_documento:
            texto += pagina.get_text()
    return texto
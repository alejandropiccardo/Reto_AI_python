# RETO 

En el marco del reto UNICEF "ni silencio ni tabú" el proyecto es crear un bot de respuesta a usuarios  relacionado a la salud mental.

# pasos para instalación:
1. Clonar repo
2. Descargar dependencias
3. Se deberá crear un archivo .env con :
    APIKEY=<tu apikey>
3. Ejecutar  ->  uvicorn main:app --reload
4. En el navegador ir a localhost:8000/docs  #donde podrás ver el swagger
5. Enviar la pregunta al bot a través del endpoint /chatbot #se recomienda "¿de qué trata el documento?

# ejemplos:

![alt text](/img/image.png)
![alt text](/img/image2.png)


# notas:
- el bot se puede alimentar del pdf incluido, sin embargo por temas de demora al crear los embeddings, simplemente escribi unas lineas , se puede ver en "info.py"
        revisar: creo que cada request, vuelve a generar los embeddings

- el bot aun no esta limitado a contestar SOLO en base a los docs

- Queda pendiente el manejo de dependencias! (perdón):(
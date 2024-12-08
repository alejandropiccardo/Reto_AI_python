from fastapi import FastAPI
import chatbot

app = FastAPI()

@app.get("/info/{message}")
async def read_item(message: str, q: str = None):
    return {"message": "hola", "q": q}

@app.post("/chatbot/")
async def chatResponse(message: str):
    rsp = chatbot.responseFromBot(message)
    return {"message": rsp}

#print(chatResponse("de q trata el documento"))
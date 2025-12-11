from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"status": "OK", "service": "GigaChat"}

@app.post("/chat")
def chat(message: str):
    return {"answer": f"Получил: {message}"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "OK", "service": "GigaChat Backend"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/chat")
async def chat(message: str):
    return {
        "answer": f"Сообщение получено: {message}",
        "status": "success"
    }

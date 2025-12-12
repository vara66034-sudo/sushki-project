from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Импорт твоей функции для работы с GigaChat
from giagachat_stuff import sendMessageFromBackend

app = FastAPI(title="СБЕР AI — Backend GigaChat")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем фронту обращаться к API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Статика фронта ---
app.mount("/", StaticFiles(directory="../../frontend/src", html=True), name="static")

# --- Модель POST-запроса ---
class ChatMessage(BaseModel):
    text: str

# --- Проверка здоровья сервиса ---
@app.get("/health")
def health():
    return {"status": "healthy"}

# --- Эндпоинт для чата ---
@app.post("/api/chat")
async def chat_endpoint(message: ChatMessage):
    """
    Получает текст от фронта, отправляет в GigaChat и возвращает ответ.
    """
    try:
        # Отправляем текст в GigaChat через твою функцию
        answer = sendMessageFromBackend(message.text)
        return {"answer": answer, "status": "success"}
    except Exception as e:
        # Если что-то пошло не так
        return {"answer": f"Ошибка: {str(e)}", "status": "error"}

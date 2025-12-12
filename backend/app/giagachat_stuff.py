from gigachat import GigaChat
import os

giga = GigaChat(
   credentials=os.getenv('GIGACHAT_API_KEY', ''),
)

def sendMessageFromBackend(text: str) -> str:
    response = giga.chat(text)
    return f"GigaChat ответил: {response.choices[0].message.content}"

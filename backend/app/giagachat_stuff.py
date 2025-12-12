from gigachat import GigaChat
import os

giga = GigaChat(
   credentials=os.getenv('GIGACHAT_API_KEY', ''),
   verify_ssl_certs=False
)

def sendMessageFromBackend(text: str) -> str:
    response = giga.chat(text)
    return f"GigaChat ответил: {response.choices[0].message.content}"

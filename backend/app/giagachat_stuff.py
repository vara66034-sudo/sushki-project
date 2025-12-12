from gigachat import GigaChat
import os

giga = GigaChat(
   credentials=os.getenv('GIGACHAT_API_KEY', ''),
   model=os.getenv('GIGACHAT_MODEL', ''),
   verify_ssl_certs=False,
)

def sendMessageFromBackend(text: str) -> str:
    response = giga.chat(text)
    return f"GigaChat ответил: {response.choices[0].message.content}"

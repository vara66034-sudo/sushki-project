import os
from dotenv import load_dotenv
from langchain_gigachat import GigaChat

load_dotenv()


def get_llm():
    auth_key = os.getenv("GIGACHAT_AUTH_KEY")

    if not auth_key:
        raise RuntimeError("❌ GIGACHAT_AUTH_KEY не найден в .env")

    return GigaChat(
        credentials=auth_key,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
        temperature=0.2,
    )

import os
import requests
from typing import Optional

class GigaChatService:
    def __init__(self):
        # Берем ключ из переменных окружения
        self.api_key = os.getenv("GIGACHAT_API_KEY")
        self.base_url = "https://gigachat.devices.sberbank.ru/api/v1"
        
    def get_access_token(self) -> Optional[str]:
        """Получить access token по API ключу"""
        try:
            auth_url = f"{self.base_url}/oauth"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = {"scope": "GIGACHAT_API_PERS"}
            
            response = requests.post(auth_url, headers=headers, data=data)
            if response.status_code == 200:
                return response.json().get("access_token")
            else:
                print(f"Ошибка аутентификации: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка получения токена: {e}")
            return None
    
    def chat(self, message: str) -> str:
        """Основной метод для общения с ГИГАЧАТ"""
        try:
            # 1. Получить access token
            access_token = self.get_access_token()
            if not access_token:
                return "Ошибка аутентификации в ГИГАЧАТ"
            
            # 2. Отправить запрос
            chat_url = f"{self.base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "GigaChat",
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 512
            }
            
            response = requests.post(chat_url, headers=headers, json=payload)
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Ошибка ГИГАЧАТ: {response.status_code}"
                
        except Exception as e:
            return f"Ошибка соединения: {str(e)}"

# Глобальный экземпляр
gigachat = GigaChatService()

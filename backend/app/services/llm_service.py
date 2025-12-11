from .gigachat_service import gigachat

class LLMService:
    def __init__(self, use_gigachat=True):
        self.use_gigachat = use_gigachat
    
    def ask(self, question: str) -> str:
        """Основной метод - используем ГИГАЧАТ"""
        if self.use_gigachat:
            return gigachat.chat(question)
        else:
            # Fallback на локальную модель если нужно
            return "Используется ГИГАЧАТ"
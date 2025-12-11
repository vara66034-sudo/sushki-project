from app.vectorstore import load_vectorstore
from app.rag_chain import run_rag
from app.llm import get_llm


def main():
    vectorstore = load_vectorstore()
    llm = get_llm()

    question = input("Вопрос: ")

    answer = run_rag(llm, vectorstore, question)
    print("\nОтвет:\n", answer)

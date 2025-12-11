def run_rag(llm, vectorstore, question: str):
    docs = vectorstore.similarity_search(question, k=4)

    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""Ответь на вопрос, используя контекст ниже.

Контекст:
{context}

Вопрос:
{question}
"""

    response = llm.invoke(prompt)
    return response.content

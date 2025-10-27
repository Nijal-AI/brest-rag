"""
Module de génération de prompts pour le RAG Brest.
Contient les fonctions de création des prompts pour le LLM.
"""


def generate_prompt(question: str, context: str) -> str:
    """
    Fonction de génération du prompt pour le LLM.
    Pour l'instant, utilise un prompt simple de question-answering.

    Args:
        question: La question originale
        context: Le contexte récupéré des documents

    Returns:
        Le prompt formaté pour le LLM
    """
    # TODO: Implémenter des prompts plus sophistiqués ici (few-shot, chain-of-thought, etc.)
    prompt_text = f"""
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question}

Context: {context}

Answer:
"""
    return prompt_text
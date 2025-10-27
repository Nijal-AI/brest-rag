"""
Module de sécurité et guardrails pour le RAG Brest.
Contient les fonctions de vérification des questions et réponses.
"""


def guardrail(question: str) -> bool:
    """
    Fonction guardrail pour vérifier la sécurité des questions.
    Pour l'instant, retourne toujours True (pas de restriction).

    Args:
        question: La question à vérifier

    Returns:
        True si la question est autorisée, False sinon
    """
    # TODO: Implémenter les vérifications de sécurité ici
    return True


def response_guardrail(response: str) -> bool:
    """
    Fonction guardrail pour vérifier la sécurité et l'adéquation des réponses générées.
    Pour l'instant, retourne toujours True (pas de restriction).

    Args:
        response: La réponse générée par le LLM

    Returns:
        True si la réponse est autorisée, False sinon
    """
    # TODO: Implémenter les vérifications de sécurité sur les réponses ici
    # (contenu inapproprié, hallucinations, etc.)
    return True
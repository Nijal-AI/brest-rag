"""
Module de reranking pour le RAG Brest.
Contient les fonctions de reranking des documents récupérés.
"""


def rerank_documents(docs: list, query: str) -> list:
    """
    Stub pour le reranking des documents récupérés.

    Args:
        docs: Liste d'objets documents renvoyés par le vector store
        query: La requête (question reformulée) utilisée pour la recherche

    Returns:
        Liste de documents ordonnés selon le score de reranking.

    Note:
        Pour l'instant cette fonction renvoie simplement la liste telle quelle.
        Plus tard, on pourra y intégrer des modèles/scorers supplémentaires
        (cross-encoders, classifiers, préférences utilisateur, etc.).
    """
    # Implémentation future : calculer un nouveau score pour chaque doc et trier
    return docs
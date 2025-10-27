"""
Module de recherche et récupération pour le RAG Brest.
Contient les fonctions de recherche dans le vector store.
"""

from langchain_core.vectorstores import InMemoryVectorStore


def retrieve_documents(vector_store: InMemoryVectorStore, query: str):
    """
    Fonction de recherche et récupération des documents pertinents.
    Pour l'instant, utilise une recherche de similarité simple.

    Args:
        vector_store: Le vector store à utiliser pour la recherche
        query: La requête de recherche (question reformulée)

    Returns:
        Liste des documents récupérés
    """
    # TODO: Implémenter une logique de recherche améliorée ici (reranking, filtres, etc.)
    retrieved_docs = vector_store.similarity_search(query, k=4)
    return retrieved_docs
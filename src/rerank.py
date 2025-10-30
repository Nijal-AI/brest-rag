"""
Module de reranking pour le RAG Brest.
Contient les fonctions de reranking des documents récupérés.
"""
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors import FlashrankRerank
from langchain_core.vectorstores import VectorStore

def rerank_documents(query: str, vector_store: VectorStore) -> list:
    """
    Fonction de reranking des documents récupérés.

    Args:
        query: La requête (question reformulée) utilisée pour la recherche
        vector_store: Le vector store à utiliser pour la recherche

    Returns:
        Liste de documents ordonnés selon le score de reranking.
    """
    # Implémentation future : calculer un nouveau score pour chaque doc et trier
    compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2", top_n=4) # type: ignore
    retriever = vector_store.as_retriever()
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )
    
    compressed_docs = compression_retriever.invoke(
        query
    )
    return compressed_docs
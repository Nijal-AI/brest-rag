
import os
os.environ['USER_AGENT'] = 'brest-rag/1.0'

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

def ingest_documents(embeddings, urls=None):
    """
    Ingère des documents depuis des URLs web de manière générique.

    Args:
        embeddings: L'objet embeddings à utiliser
        urls: Liste d'URLs à charger. Si None, utilise une URL par défaut.

    Returns:
        Le vector store initialisé avec les documents
    """
    if urls is None:
        urls = ["https://fr.wikipedia.org/wiki/Brest"]

    # Charger les documents
    loader = WebBaseLoader(web_paths=urls)
    docs = loader.load()

    # Découper les documents en chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_splits = text_splitter.split_documents(docs)

    # Ajouter des métadonnées basiques
    for doc in all_splits:
        if 'source' not in doc.metadata:
            doc.metadata['source'] = doc.metadata.get('source', 'web')

    # Indexer les chunks
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(all_splits)
    return vector_store
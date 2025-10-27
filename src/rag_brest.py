from dotenv import load_dotenv
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Charger les variables d'environnement
load_dotenv()

# Importer la fonction d'ingestion
from .script_ingestion import ingest_documents

# Importer les modules du pipeline
from .guardrail import guardrail, response_guardrail
from .reformulate import reformulate_question
from .retrieve import retrieve_documents
from .generate import generate_prompt
from .rerank import rerank_documents

# Définir les embeddings et le LLM
embeddings = OpenAIEmbeddings()
llm = ChatOpenAI()

# Initialiser le vector store via la fonction d'ingestion
vector_store = ingest_documents(embeddings)


def ask_question(question: str) -> tuple[str, list]:
    """
    Pipeline RAG complet : guardrail -> reformulation -> recherche -> reranking -> génération -> guardrail réponse.

    Args:
        question: La question de l'utilisateur

    Returns:
        Tuple de (réponse générée et validée, documents récupérés)
    """
    # 1. Vérification guardrail de la question
    if not guardrail(question):
        return "Désolé, cette question n'est pas autorisée.", []

    # 2. Reformulation de la question
    reformulated_question = reformulate_question(question)

    # 3. Recherche de documents pertinents
    retrieved_docs = retrieve_documents(vector_store, reformulated_question)

    # 4. Reranking des documents
    reranked_docs = rerank_documents(retrieved_docs, reformulated_question)

    # 5. Préparer le contexte
    context = "\n\n".join(doc.page_content for doc in reranked_docs)

    # 6. Générer le prompt
    prompt_text = generate_prompt(question, context)

    # 6. Générer la réponse avec le LLM
    response = llm.invoke(prompt_text)
    generated_response = str(response.content)

    # 7. Vérification guardrail de la réponse
    if not response_guardrail(generated_response):
        return "Désolé, la réponse générée n'est pas appropriée.", []

    return generated_response, reranked_docs
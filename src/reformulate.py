"""
Module de reformulation et contextualisation pour le RAG Brest.
Contient les fonctions de traitement des questions.
"""

from langchain_openai import ChatOpenAI

from datetime import date
import re

llm = ChatOpenAI()

def reformulate_question(question: str) -> str:
    """
    Fonction de reformulation/contextualisation des questions.
    Pour l'instant, retourne la question inchangée.

    Args:
        question: La question originale

    Returns:
        La question reformulée/contextualisée
    """
    today = date.today().strftime("%d/%m/%Y")


    response = llm.invoke("corrige les fautes dans cette question et utilise un langage soutenu : " + question)
    q = str(response.content)
    q = q.strip().lower()
    q = re.sub(r"[!?]", "", q)

    # Reformulation contextuelle simple
    if not q.endswith("?"):
        q += " ?"

    # Contextualisation adaptés au RAG de Brest
    if "brest" not in q.lower():
        q = f"Dans le contexte de la ville de Brest dans le finistère, le {today}, {q}"
    else:
        q = f"Le {today}, {q}"

    # Ajout de fin de prompt
    q += " Utilise uniquement les informations présentes dans les sources du RAG. Ne fais pas de supposition."
    q += " La réponse devra valoriser Brest en particulier son caractère maritime et être rédigée dans un langage soutenu, approprié à un musée ou à une institution culturelle."

    print(f"Prompt reformulé : {q}\n")
    return question

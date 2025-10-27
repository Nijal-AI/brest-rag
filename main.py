#!/usr/bin/env python3
"""
Interface de chat en terminal pour le RAG de Brest.
Tapez 'quit' pour quitter.
"""

from src.rag_brest import ask_question


def main():
    print("Bienvenue dans le chat RAG de Brest !")
    print("Posez vos questions sur Brest ou tapez 'quit' pour quitter.\n")

    while True:
        try:
            question = input("Vous: ").strip()
            if not question:
                continue
            if question.lower() in ['quit', 'exit', 'q']:
                print("Au revoir !")
                break

            # Utiliser la fonction RAG pour traiter la question
            answer, retrieved_docs = ask_question(question)

            # Afficher les documents récupérés
            if retrieved_docs:
                print("Documents récupérés :")
                for i, doc in enumerate(retrieved_docs, 1):
                    print(f"{i}. {doc.page_content[:200]}...")  # Limiter à 200 caractères pour la lisibilité
                print()

            print(f"RAG Brest: {answer}\n")

        except KeyboardInterrupt:
            print("\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur: {e}\n")


if __name__ == "__main__":
    main()

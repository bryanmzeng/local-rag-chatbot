import argparse
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

#PROMPT_TEMPLATE = """
#Answer the question based only on the following context:

#{context}

#---

#Answer the question based on the above context: {question}
#"""

PROMPT_TEMPLATE = """
Answer the question using the following context, which has two parts, conversation and database context, as well as your own insights:

{context}

---

Answer the following question based on the above context and your own knowledge: {question}
"""

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    parser.add_argument("--conversation", type=str, help="The conversation context.")
    args = parser.parse_args()
    query_text = args.query_text
    conversation = args.conversation if args.conversation else ""
    query_rag(query_text, conversation)


def query_rag(query_text: str, conversation: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    full_context = f"Context of Conversation history:\n{conversation}\n\n---\n\nContext from database:\n{context_text}"
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=full_context, question=query_text)
    # print(prompt)

    #change llama3 for low performing model for faster query time - potentially implement dropdown to change model
    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"{response_text}\nSources: {sources}" #use this response in print statement to see sources used from db
    print(response_text)
    return response_text


if __name__ == "__main__":
    main()

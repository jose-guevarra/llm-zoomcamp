

from dotenv import load_dotenv
load_dotenv()

from minsearch import Index
from openai import OpenAI

import rag_helper


def build_index(documents):
    index = Index(
        text_fields=['content'],
        keyword_fields=['filename']
    )
    index.fit(documents)
    return index


def search(query: str, index: Index) -> dict[str, str]:
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={'question': 3.0, 'section': 0.5},
        filter_dict={'course': 'llm-zoomcamp'}
    )


def main():
    print("Starting...")

    from gitsource import GithubRepositoryDataReader
    reader = GithubRepositoryDataReader(
        repo_owner="DataTalksClub",
        repo_name="llm-zoomcamp",
        commit_id="8c1834d",
        allowed_extensions={"md"},
        filename_filter=lambda path: "/lessons/" in path,
    )

    files = reader.read()

    # Q1. How many lesson pages
    print(f"Number of lession Pages: {len(files)}")

    documents = []
    for file in files:
        doc = file.parse()
        documents.append(doc)

    #print(documents[0]) # 01-agentic-rag/lessons/01-intro.md
    index = build_index(documents)

    question = "How does the agentic loop keep calling the model until it stops?"
    search_results = index.search(
        question,
        #boost_dict={"question": 2.0, "section": 0.5},
        #filter_dict={"course": "llm-zoomcamp"},
        num_results=5
    )

    # Q2: 01-agentic-rag/lessons/14-agentic-loop.md 
    [print(doc["filename"]) for doc in search_results]

    openai_client = OpenAI()
    assistant = rag_helper.RAGBase(
        index=index,
        llm_client=openai_client,
    )

    print("")
    answer, input_tokens = assistant.rag("How does the agentic loop keep calling the model until it stops?")
    print(f"Input Tokens used: {input_tokens}")
    print(answer)
    # Q3 - 7032 input tokens

    from gitsource import chunk_documents
    chunks = chunk_documents(documents, size=2000, step=1000)
    print("Chunks: ", len(chunks))
    # Q4 chunks 295

    index_chunked = build_index(chunks)

    question = "How does the agentic loop keep calling the model until it stops?"
    search_results = index_chunked.search(
        question,
        #boost_dict={"question": 2.0, "section": 0.5},
        #filter_dict={"course": "llm-zoomcamp"},
        num_results=5
    )

    openai_client = OpenAI()
    assistant = rag_helper.RAGBase(
        index=index_chunked,
        llm_client=openai_client,
    )

    answer, input_tokens = assistant.rag("How does the agentic loop keep calling the model until it stops?")
    print(f"Chunked Input Tokens used: {input_tokens}")
    print(answer)
    # chunked input tokens 2221 / 3x fewer

    ## Agent
    from toyaikit.llm import OpenAIClient
    from toyaikit.tools import Tools
    from toyaikit.chat import IPythonChatInterface
    from toyaikit.chat.runners import OpenAIResponsesRunner, DisplayingRunnerCallback


    agent_tools = Tools()
    agent_tools.add_tool(search)
    agent_tools.get_tools()






if __name__ == "__main__":
    main()
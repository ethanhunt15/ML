import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from llm_client import PROVIDER


# Initialize embeddings
if PROVIDER == "openai":
    embeddings = OpenAIEmbeddings()
elif PROVIDER == "gemini":
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY"))
else:
    raise ValueError("Unsupported LLM_PROVIDER. Use 'openai' or 'gemini'.")

# Initialize or load ChromaDB
DB_DIR = "chromadb_store"
vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

# Text splitter config
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def ingest_document(document_text, metadata={}):
    """
    Ingests a new document into ChromaDB after splitting.
    """
    docs = text_splitter.create_documents([document_text], metadatas=[metadata])
    vectordb.add_documents(docs)
    vectordb.persist()
    return f"Ingested {len(docs)} chunks."


def query_rag(question):
    """
    Queries ChromaDB using LangChain RetrievalQA chain with either GPT or Gemini as the LLM.
    
    Args:
        question (str): The input query.
    
    Returns:
        str: The generated answer.
    """
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    # Select LLM based on provider
    if PROVIDER == "gpt":
        llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    elif PROVIDER == "gemini":
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    else:
        raise ValueError(f"Unsupported llm_provider: {llm_provider}")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    answer = qa_chain.run(question)
    return answer

if __name__ == "__main__":
    sample_text = """
RBI Circular XYZ/2025: All PSPs must implement multi-factor authentication for merchant onboarding by Sep 2025. Non-compliance penalty is INR 5 lakh per violation.
"""
    print(ingest_document(sample_text, metadata={"source": "Sample Circular"}))
    
    response = query_rag("What is the penalty for non-compliance in merchant onboarding?")
    print("Answer:", response)

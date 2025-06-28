import chromadb
import uuid
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def store_version(content, chapter_id):
    client = chromadb.PersistentClient(path="./chromadb")
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection(
        name="book_versions",
        embedding_function=embedding_function
    )
    
    version_id = str(uuid.uuid4())
    collection.add(
        documents=[content],
        metadatas=[{"chapter_id": chapter_id, "version": "1.0"}],
        ids=[version_id]
    )
    return version_id

def search_content(chapter_id):
    client = chromadb.PersistentClient(path="./chromadb")
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_collection(
        name="book_versions",
        embedding_function=embedding_function
    )
    
    results = collection.query(
        query_texts=[chapter_id],
        n_results=1
    )
    return results["documents"][0][0] if results["documents"] else ""
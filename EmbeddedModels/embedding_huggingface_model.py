from dotenv import find_dotenv, load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv(find_dotenv())

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# One text -> one vector
vector = embeddings.embed_query("What is the capital of China?")
print("Query vector length:", len(vector))
print("First 5 values:", vector[:5])

# Many texts -> many vectors
docs = ["Beijing is the capital of China.", "Paris is the capital of France."]
doc_vectors = embeddings.embed_documents(docs)
print("Number of documents embedded:", len(doc_vectors))

from dotenv import find_dotenv, load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv(find_dotenv())

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",dimemsion=32)

# One text -> one vector
vector = embeddings.embed_query("What is the capital of China?")
#print("Query vector length:", len(vector))
#print("First 5 values:", vector[:5])
print(str(vector))

#Many texts -> many vectors
docs = ["Beijing is the capital of China.", "Paris is the capital of France."]
doc_vectors = embeddings.embed_documents(docs)
print("Number of documents embedded:", len(doc_vectors))
print(str(doc_vectors))

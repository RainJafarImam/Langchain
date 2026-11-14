from dotenv import find_dotenv, load_dotenv
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")
result = model.invoke("who is president of the China?")

print(result.text)

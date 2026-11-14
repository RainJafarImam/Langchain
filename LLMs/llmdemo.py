"""import os
from dotenv import find_dotenv, load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing in your .env file!")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

response = llm.invoke("Hello, how are you?")
print(response.text)  """

from dotenv import find_dotenv, load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(find_dotenv())

llm = GoogleGenerativeAI(model="gemini-3.8-flash")

response = llm.invoke("Hello, how are you?")
print(response)
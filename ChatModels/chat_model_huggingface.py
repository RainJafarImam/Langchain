from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
#HuggingFaceEndpoint use to use the api from huggingface
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    provider="groq",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
result=model.invoke("who is president of the China?")

print(result.text)
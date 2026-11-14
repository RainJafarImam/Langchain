from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to Hindi."),
    HumanMessage(content="I love programming.")
]


result=model.invoke(messages)
messages.append(AIMessage(content=result.text))
print(result.text)

from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv(find_dotenv())
model = ChatGroq(model="openai/gpt-oss-120b",temperature=0.7)


chat_history = [
    SystemMessage(content="You are a helpful assistant that translates English to Hindi.")
    ]
while True:
    user_input=input("you:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print("AI:",result.text)



print(chat_history)



from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")

# Template with a placeholder where the old conversation will be inserted
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent handling refund requests'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Earlier conversation about a refund (normally loaded from a file or database)
chat_history = [
    HumanMessage(content="I want a refund for my headphones, order #4521. They stopped working."),
    AIMessage(content="Sorry to hear that. I have started the refund for order #4521. It will take 5-7 working days."),
    HumanMessage(content="Okay, thank you.")
]

# Fill the placeholder and the new question
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'How long will my refund take, and which order was it for?'
})

result = model.invoke(prompt)

print(result.text)

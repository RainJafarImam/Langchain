from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
model = ChatGroq(model="openai/gpt-oss-120b")
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Doosra'})

result = model.invoke(prompt)

print(result.text)
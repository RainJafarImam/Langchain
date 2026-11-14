from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")


#1 prompt ->Detail Report
template1=PromptTemplate(
    template="write a detailed report on the following review: {topic}",
    input_variables=["topic"]
)


#2 prompt ->Summary
template2=PromptTemplate(
    template="write a5 line sumary on this given text. \n {text}",
    input_variables=["text"]
)


prompt1=template1.invoke({"topic":"black hole"})
result1=model.invoke(prompt1)

prompt2=template2.invoke({"text":result1.content})
result2=model.invoke(prompt2)


print(result1.content)
print()
print(result2.content)



# ---------- WITH StrOutputParser ----------
parser = StrOutputParser()

report_chain = template1 | model | parser | template2 | model | parser      # returns a plain string

report = report_chain.invoke({"topic": "black hole"})

print("\nWITH PARSER")
print(report)

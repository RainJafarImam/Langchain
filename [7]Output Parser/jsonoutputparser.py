import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")

# ---------- WITHOUT output parser ----------
prompt = ("Give me the name, age and city of a fictional person. "
          "Reply only with JSON using the keys name, age and city.")

raw = model.invoke(prompt)          # AIMessage object
print("WITHOUT PARSER")
print(type(raw.text))               # <class 'str'> -> just text, not a dict
data = json.loads(raw.text.strip()) # we convert to dict ourselves
print(type(data))
print("Name:", data["name"], "| Age:", data["age"], "| City:", data["city"])

# ---------- WITH JsonOutputParser ----------
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person.\n{format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser   # returns a dict directly

result = chain.invoke({})
print("\nWITH PARSER")
print(type(result))                 # <class 'dict'>
print(result)

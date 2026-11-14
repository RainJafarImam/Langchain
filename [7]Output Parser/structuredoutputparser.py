from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")

# ---------- WITHOUT output parser ----------
raw = model.invoke("Give 3 facts about black holes. Number them 1, 2 and 3.")
print("WITHOUT PARSER")
print(type(raw.text))        # <class 'str'> -> plain text, hard to use in code
print(raw.text)

# ---------- WITH StructuredOutputParser ----------
# Define the fields we want back
schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about {topic}.\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser   # returns a dict with the 3 keys

result = chain.invoke({"topic": "black hole"})
print("\nWITH PARSER")
print(type(result))                 # <class 'dict'>
print(result)
print("Fact 1:", result["fact_1"])

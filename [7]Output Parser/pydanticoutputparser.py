from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv(find_dotenv())

model = ChatGroq(model="openai/gpt-oss-120b")


# Schema: fixed keys, types and rules
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person, must be above 18")
    city: str = Field(description="City the person lives in")


# ---------- WITHOUT output parser ----------
prompt = ("Give me the name, age and city of a fictional Indian person. "
          "Reply only with JSON using the keys name, age and city.")

raw = model.invoke(prompt)                   # AIMessage object
person = Person.model_validate_json(raw.text.strip())   # we validate by hand
print("WITHOUT PARSER")
print(person)
print(person.name, person.age, person.city)

# ---------- WITH PydanticOutputParser ----------
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name, age and city of a fictional {place} person.\n{format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser            # returns a Person object

result = chain.invoke({"place": "Indian"})
print("\nWITH PARSER")
print(type(result))                          # Person object, not a dict
print(result)
print(result.name, result.age, result.city)

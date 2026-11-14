from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Runs the model locally on your PC (downloads it the first time).
# Change model_id to any Hugging Face text-generation model that fits your RAM.
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100},
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("who is president of the China?")

print(result.text)

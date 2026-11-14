from langchain_anthropic import ChatAnthropic
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
model = ChatAnthropic(model="claude-sonnet-5-5")
result = model.invoke("what is the top 5 trending model in AI in china?")
print(result.text)
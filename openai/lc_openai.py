import keys
from langchain.chat_models import init_chat_model
import os

os.environ["OPENAI_API_KEY"] = keys.OPENAIKEY

model = init_chat_model("gpt-4o-mini", model_provider="openai")
response = model.invoke("What is the capital of Spain")
print(response)
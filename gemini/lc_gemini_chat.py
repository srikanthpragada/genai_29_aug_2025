import keys 
from langchain.chat_models import init_chat_model
import os

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", 
                         model_provider="google_genai",
                         temperature = 0.7)
response = model.invoke("What is special about Real Madrid? Give me 3 bullet points")
print(response.content)

 

import keys 
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
 

os.environ["GOOGLE_API_KEY"] =  keys.GOOGLEKEY


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             temperature=0.9, 
                             max_output_tokens=50,
                             model_kwargs= { "frequency_penalty": 1.5} )
                             

response = llm.invoke(
    [HumanMessage(content="write a story about Sun. It should no more than 5 sentences")])
print(response.content)
 

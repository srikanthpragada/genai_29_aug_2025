from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
import keys

model_id = "mistralai/Mistral-7B-Instruct-v0.3"   
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

template_str = """Write a Python function for the following requirements:
{text}
"""
prompt_template = PromptTemplate.from_template(template=template_str)

prompt = prompt_template.format(
       text="Check whether a number is perfect number or not")

messages = [{"role": "user", "content": prompt}]

response = client.chat_completion(messages)
reply = response.choices[0].message.content
print(reply)

from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY)

messages = [
    {"role": "user", "content": "What is the capital of France?"}
]

response = client.chat_completion(messages)
#print(response)
print(response.choices[0].message.content)

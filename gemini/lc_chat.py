import keys 
from langchain.chat_models import init_chat_model
import os

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", 
                        model_provider="google_genai"
                        )

messages = []

while True:
    prompt = input("Query [q to quit, c to create new prompt] :")
    if prompt.lower() == 'q':
        break

    if prompt.lower() == 'c':
        messages = []
        continue 
    
    # create a message from prompt 
    messages.append({"role": "user", "content": prompt})
    ai_response = model.invoke(messages)
    response = ai_response.content
    print(response)
    print("-" * 80)

    #add response to messages as AIMessage 
    messages.append({"role": "assistant", "content": response})



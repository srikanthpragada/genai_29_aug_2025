from huggingface_hub import InferenceClient

import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY)


messages = []

while True:
    prompt = input("Query [q to quit] :")
    if prompt.lower() == 'q':
        break
    # create a message from prompt 
    messages.append({"role": "user", "content": prompt})
    ai_response = client.chat_completion(messages)
    response = ai_response.choices[0].message.content
    print(response)
    print("-" * 80)

    #add response to messages as AIMessage 
    messages.append({"role": "assistant", "content": response})



#pip install google-generativeai
#Create key using https://aistudio.google.com/apikey

import keys 
import google.generativeai as genai

genai.configure(api_key=keys.GOOGLEKEY)

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("List 5 big cities in India. Just give names.")
print(response.text)
 

from transformers import logging
logging.set_verbosity_error()  # Only show errors

import transformers.utils.logging
transformers.utils.logging.disable_progress_bar()


from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
from transformers import pipeline
import keys 



loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, 
      HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

print('Created FAISS index')

question = "What is Generative AI course fee?"

llm  = pipeline("text-generation", model="google/gemma-2b-it" , token = keys.HUGGINGFACEKEY)

retriever = db.as_retriever()
results = retriever.invoke(question)

context = "\n".join([doc.page_content for doc in results])

prompt = f"""
Please answer the question based on the context.

Context : {context}
Question: {question}
Answer: 
"""


result =  llm(prompt)
output = result[0]["generated_text"]
print( output[output.find("Answer:") + 7:].strip())

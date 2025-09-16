# Using local model through pipeline() 
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
from transformers import pipeline
import streamlit as st 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()

embeddings_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Facebook AI Similarity Search
db = FAISS.from_documents(docs,embeddings_model)

prompt_template = """:
Consider the following context and give a short answer for the given question.
If you don't find answer in the context, please say you don't know the answer.
Context: {context}
Question:{question}
Answer:
"""

prompt  = PromptTemplate.from_template(prompt_template)

#print('Created FAISS index')
retriever = db.as_retriever()


# llm = pipeline(task = "text-generation",   
#                model = "google/gemma-2b-it")

llm  = pipeline("text-generation", model="google/gemma-2b-it")


st.title("RAG Courses Demo")
query = st.text_input("Enter query :")
if len(query) > 0:
    results = retriever.invoke(query)
    matching_docs_str = "\n".join([doc.page_content for doc in results])
    final_prompt = prompt.format(context=matching_docs_str, question=query)
    result =  llm(final_prompt)
    output = result[0]["generated_text"]
    st.write(output[output.find("Answer:") + 7:].strip())
    
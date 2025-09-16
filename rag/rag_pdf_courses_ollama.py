from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

loader = PyPDFLoader(
    r"courses_offered.pdf", mode="page")

docs = loader.load()
print("Number of pages loaded: ", len(docs))

embeddings_model = OllamaEmbeddings(model="nomic-embed-text:latest")
db = FAISS.from_documents(docs, embeddings_model)

llm = OllamaLLM(model="gemma3:1b")
question = "What is the prerequisite for Generative AI course?"

matches = db.similarity_search(question, k=3)
print("Number of matches found: ", len(matches))

# create prompt with matching docs 

context = ""
for match in matches:
    context += match.page_content  + "\n\n"

prompt  =f"""
Answer the question based on the context below.
Context: {context}
Question: {question}
"""

result = llm.invoke(prompt)
print('Final Result :' + result)

from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
import keys 

# 1. Load PDF document
loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# 2. Initialize embeddings using Hugging Face Inference API
embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token= keys.HUGGINGFACEKEY
)

#  3. Create FAISS index from documents
db = FAISS.from_documents(docs, embedding_model)
 
print('Created FAISS index')



# 4.  Get access to the LLM using Hugging Face Inference API
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY, timeout=120)

# 5. Retrieve relevant documents based on the question
question = "What is course fee for Generative AI"

retriever = db.as_retriever()
results = retriever.invoke(question)

print('Search result count :', len(results))

# 6. Create prompt with context and question
context = "\n".join([doc.page_content for doc in results])

prompt = f"""
Please answer the question briefly using the context. 
If you don't find answer in the context, please say you don't know the answer.
Context : {context}
Question: {question}
"""

# 7. Make a request to LLM with the prompt (question + context)
messages = [
    {"role": "user", "content": prompt}
]

result = llm.chat_completion(messages)
print(result.choices[0].message.content)

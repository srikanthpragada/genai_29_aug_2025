import sqlite3
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
 
import keys 

db_path = r"courses.db"

def get_courses():
    # Use DBAPI
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses  # List[Tuple]

def concate_course(course):
    course_id, title, description, duration, fee, prerequisite = course
    return f"Title: {title}\nDescription: {description}\nFee: {fee}\nDuration: {duration}\nPrerequisite: {prerequisite}"

# Load courses data
courses = get_courses()

context = ""
for course in courses:
    context += concate_course(course) + "\n\n"

#print(context)

prompt_template_str = """
Answer the question based on the given context. 
Context : {context}
Question: {question}
"""

prompt_template = PromptTemplate.from_template(prompt_template_str)
prompt = prompt_template.format(context=context, 
                question="What is the duration of Generative AI course?")

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY, timeout=120)

messages = [
    {"role": "user", "content": prompt}
]

response = llm.chat_completion(messages)
print(response.choices[0].message.content)













 
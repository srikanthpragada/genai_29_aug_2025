# Access google's gemini using LangChain integrations with google 

from langchain_community.chat_models import ChatGoogleGemini

def get_gemini_model(model_name="gemini-pro", temperature=0):
    """Initialize and return a Gemini model from LangChain."""
    try:
        gemini_model = ChatGoogleGemini(model_name=model_name, temperature=temperature)
        return gemini_model
    except Exception as e:
        print(f"Error initializing Gemini model: {e}")
        return None
    
if __name__ == "__main__":
    model = get_gemini_model()
    if model:
        response = model.predict("Hello, how are you?")
        print(response) 


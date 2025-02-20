from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from .env
load_dotenv()

# Declare a Gemini model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Send a message query and get model's result
query = 'Who is the third president of Indonesia?'
result = model.invoke(query)

print(result.content)
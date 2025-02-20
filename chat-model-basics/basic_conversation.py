from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from .env
load_dotenv()

# Declare a Gemini model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Declare system messages and add an AI chat history
messages = [
    SystemMessage('Answer this question about who the president is!'),
    HumanMessage('Who is the third president of Indonesia?'),
    AIMessage('B.J. Habibie'),
    HumanMessage('What is his full name?')
]

# Send a messages and get model's result
result = model.invoke(messages)

print('AI Result:')
print(result)
print('Output Messages:')
print(result.content)  # Show only AI messages output
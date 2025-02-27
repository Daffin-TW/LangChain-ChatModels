from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()

# Declare a GPT 4o mini model
model = ChatOpenAI(model='gpt-4o-mini')

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
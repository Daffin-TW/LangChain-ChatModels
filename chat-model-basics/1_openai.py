from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()

# Declare a GPT4o mini model
model = ChatOpenAI(model='gpt-4o-mini')

# Send a message query and get model's result
query = 'Who is the third president of Indonesia?'
result = model.invoke(query)

print(result.content)
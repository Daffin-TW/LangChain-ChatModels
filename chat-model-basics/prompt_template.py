from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()

# Declare a GPT 4o mini model
model = ChatOpenAI(model='gpt-4o-mini')

# Initialize prompt with placeholders
messages = [
    ('system', 'You are a historian teacher. Make a history joke about {topic}.'),
    ('human', 'Tell me {joke_count} jokes.')
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Enter arguments for the placeholder and send a message to the model
prompt = prompt_template.invoke({'topic': 'Indonesia', 'joke_count': 2})
result = model.invoke(prompt)
# print(result)
print(result.content)
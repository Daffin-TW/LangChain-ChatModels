from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel


# Load environment variables from .env
load_dotenv()

# Declare a GPT 4o mini model
model = ChatOpenAI(model='gpt-4o-mini')

# Define prompt template
prompt_template = ChatPromptTemplate([
    ('system', 'You are an expert product reviewer.'),
    ('human', 'List the main features of the product {product_name}')
])


# Define the pros analysis step
def analyze_pros(features: str):
    pros_template = ChatPromptTemplate([
        ('system', 'You are an expert product reviewer.'),
        (
            'human',
            'Given these features: {features}, list the pros of these features.'
        )
    ])
    return pros_template.format_prompt(features=features)

# Define the cons analysis step
def analyze_cons(features: str):
    cons_template = ChatPromptTemplate([
        ('system', 'You are an expert product reviewer.'),
        (
            'human',
            'Given these features: {features}, list the cons of these features.'
        )
    ])
    return cons_template.format_prompt(features=features)

# Combine pros and cons into final review
def combine_pros_cons(pros, cons):
    return f'Pros:\n{pros}\n\nCons:\n{cons}'


# Simplify branches with LCEL
pros_branch = (
    RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()
)

cons_branch = (
    RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)

# Create a combined chain using LangChain Expression Language (LCEL)
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={'pros': pros_branch, 'cons': cons_branch})
    | RunnableLambda(lambda x: combine_pros_cons(x['branches']['pros'], x['branches']['cons']))
)

# Run the chain
result = chain.invoke({'product_name': 'vivo v9 pro'})
print(result)
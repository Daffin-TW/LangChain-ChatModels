# LangChain Basics

Welcome to the **LangChain Basics** project! This repository provides a simple introduction to using LangChain for building language model applications. The content covers basic conversations, prompt templates, and chains to get you started.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Basic Conversation](#basic-conversation)
- [Prompt Templates](#prompt-templates)
- [Chains](#chains)

## Introduction
LangChain is a framework for developing applications powered by language models. It enables easy integration of LLMs with prompts, templates, chains, and other components to build interactive applications.

## Installation
To install the necessary dependencies, run the following commands:

```bash
pip install langchain openai
```

Make sure you have an API key from OpenAI or other supported providers.

## Basic Conversation
To initiate a simple conversation with a language model:

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat_model = ChatOpenAI()
message = HumanMessage(content="Hello, how can you assist me today?")
response = chat_model([message])
print(response.content)
```

## Prompt Templates
Prompt templates help structure inputs to the model in a reusable way.

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["name"],
    template="What is the favorite color of {name}?"
)
formatted_prompt = prompt.format(name="Alice")
print(formatted_prompt)
```

## Chains
Chains allow you to combine multiple components into a single workflow.

```python
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat_model = ChatOpenAI()
prompt = PromptTemplate(input_variables=["question"], template="{question}")
chain = LLMChain(llm=chat_model, prompt=prompt)
response = chain.run("What is the capital of France?")
print(response)
```

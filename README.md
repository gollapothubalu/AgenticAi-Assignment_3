# Assignment 3 - Prompt Engineering

## Student Assignment

This assignment demonstrates three prompt engineering techniques using an LLM API.

## 1. Few-Shot Prompting

File:
`few_shot_sentiment.py`

The program classifies a customer message as Positive, Negative, or Neutral.

It uses three example inputs and expected outputs before asking the LLM to classify a new customer message.

Expected result:
`Positive`

## 2. Chain-of-Thought Prompting

File:
`chain_of_thought.py`

The program sends a mathematical word problem to the LLM and asks it to solve the problem step by step.

Expected final answer:
`60 notebooks`

## 3. Persona + Hallucination + Document

File:
`persona_document.py`

The program gives the LLM a Python Tutor persona and a document containing information about Python.

The LLM is instructed to answer only from the provided document.

Two questions are tested:

1. A question whose answer exists in the document.
2. A question whose answer does not exist in the document.

For unavailable information, the program returns:

`I don't know based on the provided document.`

## Technologies Used

- Python
- OpenAI Python SDK
- LLM API
- Few-Shot Prompting
- Chain-of-Thought Prompting
- Persona Prompting
- Hallucination Control

## Files

- `few_shot_sentiment.py`
- `chain_of_thought.py`
- `persona_document.py`
- `README.md`
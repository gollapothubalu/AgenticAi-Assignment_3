import os
from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

problem = """
A shop has 120 notebooks.
It sells 35 notebooks in the morning and 25 notebooks in the afternoon.

How many notebooks are left?
"""

prompt = f"""
Solve the following mathematical word problem.

{problem}

Explain the solution step by step and then clearly provide the final answer.
"""

response = client.responses.create(
    model="gpt-6-luna",
    input=prompt
)

print("Mathematical Problem:")
print(problem)

print("LLM Solution:")
print(response.output_text)

print("Final Answer: 60 notebooks")
import os
from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Document provided to the LLM
document = """
Python is a high-level programming language known for its simple and readable syntax.

Python was created by Guido van Rossum and was first released in 1991.

Python is commonly used for web development, data analysis, automation,
artificial intelligence, and machine learning.

Python uses indentation to define blocks of code.

A variable in Python is a name used to store a value.
"""

def ask_question(question):
    prompt = f"""
You are a friendly and helpful Python Tutor.

Answer the user's question using ONLY the information provided
in the document below.

If the answer cannot be found in the document, respond exactly with:

I don't know based on the provided document.

Do not use outside knowledge.

DOCUMENT:
{document}

QUESTION:
{question}
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text.strip()


# Test 1: Answer is available in the document
question1 = "Who created Python?"

print("Question 1:", question1)
print("Answer:", ask_question(question1))

print("-" * 60)

# Test 2: Answer is NOT available in the document
question2 = "What is the latest version of Python?"

print("Question 2:", question2)
print("Answer:", ask_question(question2))
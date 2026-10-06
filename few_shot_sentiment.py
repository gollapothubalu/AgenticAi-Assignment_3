import os
from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Few-shot examples
prompt = """
You are a customer sentiment classifier.

Your task is to classify the customer message into exactly one of:
Positive
Negative
Neutral

Here are some examples:

Example 1:
Customer message: "The product arrived early and I am very happy with it."
Sentiment: Positive

Example 2:
Customer message: "The product is damaged and the delivery was very late."
Sentiment: Negative

Example 3:
Customer message: "I received the product today. It is working normally."
Sentiment: Neutral

Now classify this new customer message:

Customer message: "The service was excellent and the support team solved my problem quickly."

Return only the sentiment label.
"""

response = client.responses.create(
    model="gpt-6-luna",
    input=prompt
)

print("Customer Sentiment:", response.output_text.strip())
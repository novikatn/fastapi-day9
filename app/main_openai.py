import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_BASE_URL"))

response = client.chat.completions.create(
    model="x-ai/grok-4",
    messages=[
        {"role": "system", "content": "You are product manager"},
        {"role": "user", "content": "What product AI is being hype?"},
    ],
)

print(response.choices[0].message.content)

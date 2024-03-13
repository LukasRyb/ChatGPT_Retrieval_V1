import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Create an OpenAI client with the API key
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a tech lead"},
        {"role": "user", "content": "This is a test prompt please confirm if it reaches you"}
    ]
)

print(completion.choices[0].message)
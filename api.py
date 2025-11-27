from dotenv import load_dotenv
from os import getenv
from openai import OpenAI

load_dotenv() # Load environment variables

ENDPOINT = "https://models.github.ai/inference"
TOKEN = getenv("GITHUB_TOKEN")


client = OpenAI(api_key=TOKEN, base_url=ENDPOINT)

# Pass in a dictionary of messages to instruct an OpenAI Model on what to do

def requestOpenAI(messages):
    response = client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model="openai/gpt-4o"
    )

    return response.choices[0].message.content

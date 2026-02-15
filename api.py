from google import genai
from google.genai import types
from dotenv import load_dotenv
from os import getenv
from openai import OpenAI

load_dotenv() # Load environment variables

ENDPOINT = "https://models.github.ai/inference"
TOKEN = getenv("GITHUB_TOKEN")

# Clients
openai_client = OpenAI(api_key=TOKEN, base_url=ENDPOINT)
gemini_client = genai.Client(api_key=getenv("GEMINI_KEY"))

# Pass in a dictionary of messages to instruct an AI Model from OpenAI
def requestOpenAI(messages):
    # Creates a chat with an OpenAI Natural Language Processor
    response = openai_client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1500,
        model="openai/gpt-4o"
    )

    # Returns AI response
    return response.choices[0].message.content

# Pass in a dictionary of messages to instruct an AI Model from Google
def requestGoogle(message, instruction, model):
    
    # Creates chat with a
    response = gemini_client.models.generate_content(
        model=model,
        contents=f"""Instruction: {instruction}\n Prompt: {message}\n"""
    )
    # Returns AI response
    return response.text

# Makes a request to an NLP from OpenAI or Google
def requestAI(messages, type, ai_type="OpenAI"):
    if ai_type == "OpenAI":
        return requestOpenAI(messages)
    elif ai_type == "Google":
        system_instruction = ""
        prompt = ""
    
        for message in messages:
            if message["role"] == "system":
                system_instruction = message["content"]
            elif message["role"] == "user":
                prompt = message["content"]
        print(system_instruction)
        google_model = "gemma-3-12b-it" if type == "agent" else "gemini-2.5-flash-lite"
        return requestGoogle(prompt, system_instruction, google_model)
from api import requestAI
from preprocess import pre_process_gemini_agent
"""
This file is used to instruct Artificial Intelligence to return
a JSON object. It determines an 'agentResponse', function, and arguments
for those functions. This object is analyzed at the front-end to make
execute code.
"""

def agent_request(user_prompt, ai_model="OpenAI"):
    # Retrieves instructions for prompting the Artificial Intelligence
    file_path = "gemini_agent" if ai_model == "Google" else "openai_agent"
    with open(f"instructions/{file_path}.txt") as f:
        SYSTEM_INSTRUCTION = f.read()
    

    messages = [{ "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": user_prompt }]

    # This is specifically for output given by Gemini
    # Gemini may return a string that can't be parsed by JSON
    response = pre_process_gemini_agent(requestAI(messages, ai_type=ai_model, type="agent"))

    return response


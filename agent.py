from api import requestAI

"""
This file is used to instruct Artificial Intelligence to return
a JSON object. It determines an 'agentResponse', function, and arguments
for those functions. This object is analyzed at the front-end to make
execute code.
"""

def agent_request(user_prompt, language="english", ai_model="OpenAI"):
     # Retrieves instructions for prompting the Artificial Intelligence
    with open("instructions/openai_agent.txt") as f:
        SYSTEM_INSTRUCTION = f.read()+ f"The agentResponse should be in {language}"
    

    messages = [{ "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": user_prompt }]

    response = requestAI(messages, ai_type=ai_model, type="agent")

    return response


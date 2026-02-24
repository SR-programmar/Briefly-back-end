from api import requestAI

# Gives instructions to Artificial intelligence to act as an AI Agent
# web assistant that can answer simple questions 
# and perform browser operations

def agent_request(user_prompt, ai_model="OpenAI"):

    # Retrieves instructions for prompting the Artificial Intelligence
    with open("instructions/openai_agent.txt") as f:
        SYSTEM_INSTRUCTION = f.read()
    messages = [{ "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": user_prompt }]

    response = requestAI(messages, ai_type=ai_model, type="agent")

    return response


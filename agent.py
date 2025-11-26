from api import requestGPT4

# Seperate chat to an AI agent that acts as a Siri-like Web browser assistant
# That can answer simple questions but also perform browser operations
def agent_request(user_prompt):

    messages = []

    response = requestGPT4(messages)

    return response
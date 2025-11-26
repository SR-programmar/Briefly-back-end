from api import requestGPT4

# Seperate chat to an AI agent that acts as a Siri-like Web browser assistant
# That can answer simple questions but also perform browser operations
def agent_request(user_prompt):

    SYSTEM_INSTRUCTION = """
    You are an A.I agent that can answer questions as well as perform browser operations. 
    You should not do anything else than what’s instructed. 
    The user will send a text response, and you will determine if the user is looking for
      an answer, or trying to perform a browser operation. Here are the browser operations
        as well as what it does. You are required to return an integer based on the function:


    IlistTabs() - list all the tabs in the browser, index 0
    openUrl() - openUrl in the current tab, return an argument called url, index 1

    You should return your response in a JSON format, here’s the template json:
    {
    “Response”: [response for the user in string format],
    “Index”: [return -1 if there’s no index, else return the index of the function]
    “Call_function”: [true/false]
    “Arguments”: [only return this if the function requires an argument]
    }


    """

    messages = [{ "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": user_prompt }]

    response = requestGPT4(messages)

    return response


if __name__ == "__main__":
    question = agent_request("Can you explain to me the difference between GTX and RTX for nvidia's GPUS")

    function_c = agent_request("Hi, can you open up the website youtube?")

    print("Summarizing...")

    print(question)

    print(function_c)


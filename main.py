### Modules ###
from flask import Flask, request, jsonify
from summarizer import AI_summarization
from agent import agent_request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, methods=["POST"])


@app.route("/")
def root_url():
    return "<h1>Get</h1>"

# Function called at root url
@app.route("/ai-sum", methods=["POST"])
def AI_summary_call():
    data = request.get_json()

    summary = AI_summarization(data["input"], data["length"], data["sum_type"])

    response = {"summary": summary}

    return jsonify(response)

# This is an extractive based summarization method
# That is used for when developers want to avoid getting rate-limited

@app.route("/simple-sum", methods=["POST"])
def simple_summary_call():

    data = request.get_json()

    summary = f"This is a test summary for developers. The summary-length is {data["length"]} and the summary type is {data["sum_type"]}"

    response = {"summary": summary}

    return jsonify(response)
    
# When user prompts the agent
@app.route("/agent-call", methods=["POST"])
def agent_call():
    data = request.get_json()

    agent_response = agent_request(data["input"])
    response = {"response": agent_response}


    return jsonify(response)

# Used for developers to make calls without utilizing OpenAI API
@app.route("/simple-agent-call", methods=["POST"])
def simple_agent_call():

    #"response":"[\n  {\n    \"agentResponse\": \"Hello! How can I assist you today?\",\n    \"index\": -1\n  }\n]"
    # Make sure agent_response is a string
    # This resulted in an error when it wasn't
    agent_response = "[{\"agentResponse\": \"This is the simple agent call. How can I assist you today\", \"index\": -1}]"

    response = {"response": agent_response}


    return jsonify(response)

    
    

if __name__ == '__main__':
    # Don't use debug=True in production!!!
    app.run(debug=False)



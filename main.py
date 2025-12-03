### Modules ###
from flask import Flask, request, jsonify
from summarizer import summarize_content, AI_summarization
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

    summary = AI_summarization(data["input"], data["mode"])

    response = {"summary": summary}

    return jsonify(response)

# This is an extractive based summarization method
# That is used for when developers want to avoid getting rate-limited

@app.route("/simple-sum", methods=["POST"])
def simple_summary_call():

    data = request.get_json()

    summary = summarize_content(data["input"], data["mode"])

    response = {"summary": summary}

    return jsonify(response)
    
# When user prompts the agent
@app.route("/agent-call", methods=["POST"])
def agent_call():
    data = request.get_json()

    agent_response = agent_request(data["input"])
    response = {"response": agent_response}


    return jsonify(response)

    
    

if __name__ == '__main__':
    # Don't use debug=True in production!!!
    app.run(debug=False)



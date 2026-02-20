### Modules ###

# Third-party packages
from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator

# Local Modules
from summarizer import AI_summarization
from agent import agent_request



app = Flask(__name__)
# Allows other origins to make POST requests to this server
CORS(app, methods=["POST"])

# Function called at root url
@app.route("/")
def root_url():
    return "<h1>Get</h1>"

### ================================ End Points ================================ ###

# Endpoint takes in webpage content and summarizes it with specified parameters
@app.route("/ai-sum", methods=["POST"])
def AI_summary_call():
    data = request.get_json()

    selected_language = "spanish" if data["language"] == "spanish" else "english"
    summary = AI_summarization(data["input"], data["length"], data["sum_type"],
                               language=selected_language)

    response = {"summary": summary}

    return jsonify(response)

"""
 
This is an endpoint used for testing
That is used for when developers want to avoid getting rate-limited
    
"""

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
    selected_language = "spanish" if data["language"] == "spanish" else "english"
    agent_response = agent_request(data["input"], language=selected_language)
    response = {"response": agent_response}


    return jsonify(response)

# Used for developers to make calls without utilizing OpenAI API
@app.route("/simple-agent-call", methods=["POST"])
def simple_agent_call():

    agent_response = "[{\"agentResponse\": \"This is the simple agent call. How can I assist you today\", \"index\": -1}]"

    response = {"response": agent_response}


    return jsonify(response)

@app.route("/english-to-spanish", methods=["POST"])
def english_to_spanish():
    data = request.get_json()
    translated = GoogleTranslator(source="auto", target="es").translate(data["text"])
    print(translated)
    return jsonify({"translatedText": translated})



### ================================ End of End Points ================================ ###

    

if __name__ == '__main__':
    # Don't use debug=True in production!!!
    app.run(debug=False)



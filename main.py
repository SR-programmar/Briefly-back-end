### Modules ###

# Third party
from flask import Flask, request, jsonify
from flask_cors import CORS

# My modules
from summarizer import summarize_content
from text_to_speech import text_to_speech

app = Flask(__name__)

CORS(app, methods=["POST"])

# Function called at root url
@app.route("/", methods=["POST"])
def home_page():

    if request.method == "POST":

        data = request.get_json()

        summary = ""
       
        if data["strict"]:
            summary = summarize_content(data["input"], 5)
        elif not data["strict"]:
            summary = text_to_speech(summarize_content(data["input"], 5), data["gender"])

        
        # summaryb64 = text_to_speech(summary)
        
        response = {"summary": summary}

        return jsonify(response)


# Run only if this is the file being run
if __name__ == '__main__':
    app.run(debug=True) # Don't use debug=True in production!!!



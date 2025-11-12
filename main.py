### Modules ###
from flask import Flask, request, jsonify
from summarizer import summarize_content

app = Flask(__name__)

# Function called at root url
@app.route("/", methods=["POST"])
def home_page():

    if request.method == "POST":
        data = request.get_json()
        summary = summarize_content(data, 5)
        response = {"summary": summary}
        return jsonify(response)
    

if __name__ == '__main__':
    # Don't use debug=True in production!!!
    app.run(debug=False)



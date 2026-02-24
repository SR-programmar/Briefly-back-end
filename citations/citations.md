# Citations

This readme includes code, python packages, and websites we used
to create this server that we didn't create.

## OpenAI API Code

**File:** api.py [def requestOpenAI(messages)]<br>
**Code:** We learnt how to make API calls to an AI model from OpenAI derived from the Github marketplace<br>
The code sample can be viewed once you click the green button that says "User this Model"<br>
**Website:** Github<br>
**Accessed:** November<br>
**URL:** [OpenAI GPT-4o Github marketplace]("https://github.com/marketplace/models/azure-openai/gpt-4o")<br>

## Gemini API Code

**File:** api.py [def requestGoogle(message, instruction, model)]<br>
**Code:** We learnt how to make API calls to an AI model from Google by using a<br>
code sample provided from the documentation<br>
**Website:** Github<br>
**Accessed:** February<br>
**URL:** [Gemini API quickstart]("https://ai.google.dev/gemini-api/docs/quickstart")<br>

### Gemini API Key

We used a python package called "google-genai" which is a tool
used to access Google's generative models. We were able to do so with an API key that
was created with [Google AI Studio]("https://aistudio.google.com/")

## Python packages

**Package:** Flask <br>
**Use:** the main part of our server is written in Flask. It's what allows it
to receive POST requests from scripts. We didn't copy and paste any code directly
from the Flask website but we're listing it as a source.<br>
**URL:** [Flask Website](https://flask.palletsprojects.com/en/stable/)<br>

**Package:** Deep-Translator<br>
**Use:** Our software provides users with the option to choose between Spanish and English<br>
This useful Python package allows us to translate english into different languages, like Spanish.<br>
**URL:** [Deep Translator](https://pypi.org/project/deep-translator/)<br>

## Hosting platform

Our server is hosted on [Vercel](https://vercel.com/)

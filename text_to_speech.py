from base64 import b64decode
from speechify import Speechify
from dotenv import load_dotenv
from os import getenv

load_dotenv() # Loads environment variable

token = getenv("SPEECHIFY_API_KEY")

speechify_api = Speechify(token=token)

# Decodes base64 text into bytes
def decode_b64(b64Text):
    return b64decode(b64Text)

# Creates a text file with base64 data to avoid overusing API
def create_test(audio_data):
    with open("test.txt", "w") as f:
        f.write(audio_data)

# Converts a 'string' text and converts it into a base64 representation
def text_to_speech(text, gender):

    voice_id = ""

    # Voice can only be male or female.
    # If it isn't, return a string explaing error

    if gender == "male":
        voice_id = "oliver"
    elif gender == "female":
        voice_id = "lisa"
    else:
        voice_id = "error"

    if voice_id != "error":
        speech = speechify_api.tts.audio.speech(
            input=text,
            voice_id=voice_id,
            audio_format="mp3",
            language="en-US"
        )

        return speech.audio_data
    else:
        return "Invalid voice_id"

if __name__ == "__main__":
    pass

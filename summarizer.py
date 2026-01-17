
### AI Summarizer ###
from api import requestOpenAI

# Summarizes the webpage's content using OpenAI's model
def AI_summarization(webpage_content, length):

    # If mode is long
    char_amt = "1000 characters"

    ### Different types of summary lengths depending on user preference ###
    if length == "Two-Sentence":
        char_amt = "two sentences"
    elif length == "Medium":
        char_amt = "500 characters"
    elif length == "Short":
        char_amt = "250 characters"

    SYSTEM_INSTRUCTION = f"""
    You are a helpful assistant that summarizes the content of the webpage.
      The summary is intended to help blind users read the contents of the webpage faster than a screenreader. 
      You will be getting a messy input that’s the .textContent of the whole webPage. 
      You are required to organize it, find the most important things to 
      include in the summary (e.g. navigation, footer, header, important articles etc.). 
      You are not to include anything unimportant in the summary. 
      The summary should be very descriptive of the webpage and should be very brief so the 
      user doesn’t have to listen for that long. You should only return the summary and don’t speak of anything else.
      Don’t include asterisks and the summary should be atleast {char_amt} and below. Do not put “Summary: “ at the beginning.

"""

    messages = [
            { "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": webpage_content }
        ]

    response = requestOpenAI(messages)

    return response


if __name__ == "__main__":
    lines = ""

    with open("cnt.txt", "r", encoding="utf-8") as f:
        for line in f:
            lines += line

    print("Summarizing...")
    # print(f"{AI_summarization(lines, "Long")}")
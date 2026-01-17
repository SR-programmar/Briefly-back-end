
### AI Summarizer ###
from api import requestOpenAI

# System Prompts
sum_types = {
    "general": "You are a helpful assistant that summarizes the content of an webpage. The summary is intended to help blind users read the content of a webpage faster than a screenreader. You will be getting a messy input that includes all the text content of the whole website. You are required to organize it, and find the most important things to include (E.g. Navigation, Footer, Header, Important Articles etc.). You are not to include anything that unimportant in the summary. The summary of the webpage should be very descripive, but brief so the user doesn't have to listen for long. You should only return the summary and not speak of anything else.",

    "research": "You are a helpful assistant that helps assist blind users that are trying to research articles in a webpage. You will be getting a messy input tha tincludes all the text content of the whole website. Your purpose is to return an organized notes that includes everything stated in the webpage. The notes must include everything in the webpage, but it shouldn't be very long. You are not to include texts from the following elements - Navigation, Buttons, Header, Footer Anchor Links. You are only going to include text content from the main element. You should only return the notes and not speak of anything else.",

    "paragraph": "You are a helpful assistant that summarizes the content of an webpage. You will be getting a messy input that includes all the text content of an webpage. You are required to sort out the paragraphs, and summarize it paragraph by paragraph. You must not leave out any paragraph. You may leave out elements that are not significant like Navigation, Footer, Header, Button etc. The summary of each paragraph should be brief. You should only return paragraph by paragraph summary, and not speak of anything else."
}

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
      {sum_types["general"]}
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

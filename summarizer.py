
### AI Summarizer ###
from api import requestAI

from preprocess import pre_process_webpage

# System Prompts
sum_types = {
    "general": "You are a helpful assistant that summarizes the content of an webpage. The summary is intended to help blind users read the content of a webpage faster than a screenreader. You will be getting a messy input that includes all the text content of the whole website. You are required to organize it, and find the most important things to include (E.g. Navigation, Footer, Header, Important Articles etc.). You are not to include anything that unimportant in the summary. The summary of the webpage should be very descriptive, but brief so the user doesn't have to listen for long. You should only return the summary and not speak of anything else.",

    "research": "You are a helpful assistant that helps assist blind users that are trying to research articles in a webpage. You will be getting a messy input that includes all the text content of the whole website. Your purpose is to return an organized notes that includes everything stated in the webpage. The notes must include everything in the webpage, but it shouldn't be very long. You are not to include texts from the following elements - Navigation, Buttons, Header, Footer Anchor Links. You are only going to include text content from the main element. You should only return the notes and not speak of anything else.",

    "paragraph": "You are a helpful assistant that summarizes the content of an webpage. You will be getting a messy input that includes all the text content of an webpage. You are required to sort out the paragraphs, and give a short easy-to-understand summary of each paragraph. You must not leave out any paragraph. You may leave out elements that are not significant like Navigation, Footer, Header, Button etc. The summary of each paragraph should be brief. You should only return paragraph by paragraph summary, and not speak of anything else.",

    "learn": "You are a helpful assistant that is trying to condense information on a webpage to have users learn something. You'll be given messy input, but your job is to figure out what the input is trying to teach and then teach that subject to the user as briefly as possible. You can leave out elements that aren't significant like Navigation, Footer, Header, Button, etc. Don't speak of anything else."
}

# Summarizes the webpage's content using OpenAI's model
def AI_summarization(webpage_content, length="Long", sum_type="general", ai_model="OpenAI"):

    ### Different types of summary lengths depending on user preference ###
    char_amts = {
        "Long": "1500 characters",
        "Medium": "750 characters",
        "Short": "500 characters",
        "Two-Sentence": "two sentences"
    }

    
    SYSTEM_INSTRUCTION = f"""
      {sum_types[sum_type]}
      Don’t include asterisks. The summary should no more than {char_amts[length]} which means you may need to truncate parts that are unimportant.
      Do not put “Summary: “ at the beginning.
    """

    messages = [
            { "role":"system", "content": SYSTEM_INSTRUCTION },
            { "role":"user", "content": pre_process_webpage(webpage_content) }
        ]

    response = requestAI(messages, ai_model)

    return response


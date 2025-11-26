### Modules ###
import nltk

### Weak Summarizer ###
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

### AI Summarizer ###
from api import requestGPT4

# Converts summary object into a string
def summary_to_string(summary):
    formatted_sum = ""

    for item in summary:
        formatted_sum += f"{str(item)}\n"
    
    return formatted_sum

# Summarizes the content using extractive summarization
def summarize_content(text_string, sentence_amt=2):
    nltk.download("punkt_tab")
    lex_sum = LexRankSummarizer()
    parser = PlaintextParser.from_string(text_string, Tokenizer("english"))


    summary = lex_sum(parser.document, sentence_amt)
    
    return summary_to_string(summary)

# Summarizes the webpage's content using OpenAI's model
def AI_summarization(text_string):
    messages = []

    response = requestGPT4(messages)

    return response


if __name__ == "__main__":
    pass
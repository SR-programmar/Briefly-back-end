"""

This file includes logic to preprocess the content
of a webpage before sending it to AI

"""

# Converts a list into a large string
def listToString(list):
    conversion = ""
    for item in list:
        conversion += f"{item}\n"
    
    return conversion

# Pre processes the text content of a webpage
# To avoid errors and minimize tokens
def pre_process_webpage(webpage_content):

    processed_lines = []
    
    for line in webpage_content.splitlines():

        # Removes all whitespace
        line = line.strip()

        # Line must be at least 3 characters long
        # Line can't be whitespace
        if not line.isspace() and len(line) > 3:
             processed_lines.append(line.lower())

    processed_page = listToString(processed_lines)

    # API can only handle up to 8000 tokens
    if len(processed_page) > 20000:
         processed_page = processed_page[:19900] + "..."

    return processed_page
    
### Testing ###
if __name__ == "__main__":
    lines = ""

    with open("cnt.txt", "r", encoding="utf-8") as f:
            for line in f:
                lines += line


import re


# Function to remove hyperlinks from markdown text
def remove_links(markdown_text):
    # Regex pattern to find [text](url)
    link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    # Dictionary to store text-to-url mappings
    links = {}

    # Function to replace the links and store the mappings
    def replace_link(match):
        text, url = match.groups()
        links[text] = url  # Store the mapping of text -> url
        return text  # Return just the plain text

    # Replace all markdown links with plain text
    plain_text = link_pattern.sub(replace_link, markdown_text)
    return plain_text, links


# Function to reinsert hyperlinks into text based on stored links
def reinsert_links(plain_text, links):
    for text, url in links.items():
        # Replace the plain text with markdown-style link
        plain_text = plain_text.replace(text, f"[{text}]({url})")
    return plain_text

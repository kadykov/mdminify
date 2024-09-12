import re
import json


# Function to remove hyperlinks from markdown text and store text-to-url mappings
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


# Function to read markdown from file, remove links, and save plain text and links
def process_markdown_file(input_md_file, output_md_file, output_json_file):
    # Read markdown content from input file
    with open(input_md_file) as file:
        markdown_text = file.read()

    # Remove links from the markdown content
    plain_text, links = remove_links(markdown_text)

    # Save plain text to output markdown file
    with open(output_md_file, "w") as file:
        file.write(plain_text)

    # Save links to a JSON file
    with open(output_json_file, "w") as file:
        json.dump(links, file, indent=4)


# Function to restore links from JSON and plain markdown file, then save the restored markdown
def restore_links_from_json(plain_md_file, json_file, output_md_file):
    # Read plain text from markdown file
    with open(plain_md_file) as file:
        plain_text = file.read()

    # Load links from JSON file
    with open(json_file) as file:
        links = json.load(file)

    # Reinsert the links into the plain text
    restored_text = reinsert_links(plain_text, links)

    # Save the restored markdown content to output file
    with open(output_md_file, "w") as file:
        file.write(restored_text)

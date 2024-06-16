def parse_entry(entry):
    """Parse an entry into its components."""
    parts = entry.strip().split(';')
    if len(parts) != 4:
        raise ValueError("Each entry must have exactly four parts separated by ';'")
    return parts[0], parts[1], parts[2], parts[3]

def format_markdown_entry(author, link, citations, comments):
    """Format a single entry into Markdown on one line."""
    base_sentence = f"- [{author}]({link}) (Citations: {citations})"
    if comments:
        return f"{base_sentence} - {comments}"
    return base_sentence


def process_input_file(input_file):
    """Process the input file and generate Markdown output."""
    with open(input_file, 'r') as file:
        content = file.read().strip()
    entries = content.split('\n')  # Assuming each entry is separated by a blank line
    markdown_output = ""
    for entry in entries:
        author, link, citations, comments = parse_entry(entry)
        markdown_output += format_markdown_entry(author, link, citations, comments) + "\n"
    return markdown_output

print("### Prefetch-based Solutions")
input_file = 'prefetch.txt' 
markdown_output = process_input_file(input_file)
print(markdown_output)

print("### Domain-specific Solutions")
input_file = 'domainspecific.txt' 
markdown_output = process_input_file(input_file)
print(markdown_output)
print("### General-purposed Solutions")
input_file = 'general.txt'
markdown_output = process_input_file(input_file)
print(markdown_output)



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

print("### Background and Motivation")
print("Indirect memory accesses arise in many emerging and important domains, including sparse deep learning, graph analytics, database processing and scientific computing.")
print("They became a bottleneck in the performance of modern computer systems because the indirect patterns are hard to predict and prefetch. Those indirect memory accesses will cause a large number of cache misses and memory stalls, which will significantly degrade the performance of the system.")
print("We have categorized related papers into two categories: Software-based and Hardware-based solutions.")
print("### Software-based Solutions")
input_file = 'software.txt' 
markdown_output = process_input_file(input_file)
print(markdown_output)
print("### Hardware-based Solutions")
input_file = 'hardware.txt' 
markdown_output = process_input_file(input_file)
print(markdown_output)
print("### Software Hardware Co-design Solutions")
input_file = 'sw-hw.txt'
markdown_output = process_input_file(input_file)
print(markdown_output)

print("### Conclusion")
print("Prefetcher: cons1: Redundant memory accesses and similar computations to the cores")
print("Prefetcher: cons2: If cannot prefetch correctly, will pollute the cache")

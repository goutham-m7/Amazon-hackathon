import re

# Read the text snippets
with open('new.txt', 'r') as f:
    text_snippets = [line.strip() for line in f.readlines() if line.strip()]

print("Text snippets:")
print(text_snippets)

# Updated regular expression pattern
pattern = r'.*?(\d+[a-zA-Z].+)'

# Function to process each term
def process_term(term):
    match = re.search(pattern, term)
    if match:
        return match.group(1)
    return None

# Process all terms and filter out None results
results = []
for snippet in text_snippets:
    # Split the snippet into individual terms
    terms = snippet.replace('[', '').replace(']', '').replace("'", "").split(', ')
    for term in terms:
        result = process_term(term)
        if result:
            results.append(result)
        print(f"Term: {term}, Result: {result}")

print("\nFinal results:")
print(results)
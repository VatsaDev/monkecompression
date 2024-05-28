import string
from collections import Counter

# Function to split text into non-overlapping chunks of a specified length
def split_into_chunks(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Open the file and read the content
file_path = "C:\\Users\\vatsa\\Desktop\\projects\\monkeComp\\monkeC2.txt"
with open(file_path, 'r') as f:
    content = f.read()

# Split the content into chunks of length 32
chunks = split_into_chunks(content, 32)

# Find the top 80 most common chunks
chunk_counts = Counter(chunks)
top_chunks = chunk_counts.most_common(80)

# Create a dictionary mapping each chunk to numbers 10-99
replacement_dict = {chunk: str(number) for chunk, number in zip([chunk for chunk, count in top_chunks], range(10, 90))}

# Replace the top 80 most common chunks in the original content
modified_content = content
for chunk, number in replacement_dict.items():
    modified_content = modified_content.replace(chunk, number)

# Print the dictionary and the modified content
print("Replacement Dictionary:")
for chunk, number in replacement_dict.items():
    print(f"'{chunk}': '{number}'")

# Write the modified content to a new file
output_file_path = "C:\\Users\\vatsa\\Desktop\\projects\\monkeComp\\monkeC3.txt"
with open(output_file_path, 'w') as f2:
    f2.write(modified_content)

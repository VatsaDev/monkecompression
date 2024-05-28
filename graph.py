import os
import matplotlib.pyplot as plt
from collections import Counter

# Define the path to the folder and block length
folder_path = 'data'
block_length = 32  # You can change this to any block length you need

# Get the list of files in the folder
files = os.listdir(folder_path)
files.sort()

# Initialize a counter to keep track of binary string occurrences
binary_counter = Counter()

c = 0

# Process each file in the folder
for file in files:
    first_file_path = os.path.join(folder_path, file)

    with open(first_file_path, 'rb') as f:
        content = f.read()
        b_content = ''.join(format(byte, '08b') for byte in content)

        # Break the binary content into blocks of the specified length
        for i in range(0, len(b_content), block_length):
            block = b_content[i:i + block_length]
            if len(block) == block_length:  # Ensure the block is of the correct length
                binary_counter[block] += 1
                
    c += 1
    if c % 100 == 0:
        print(c)

# Get the top 20 most common binary strings and their counts
top_20_binary_strings = binary_counter.most_common(20)

# Separate the binary strings and their counts for plotting
binary_strings, counts = zip(*top_20_binary_strings)

# Plot the distribution of the top 20 binary strings
plt.figure(figsize=(15, 8))
plt.bar(binary_strings, counts)
plt.xlabel('Binary String')
plt.ylabel('Count')
plt.title(f'Top 20 {block_length}-bit')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

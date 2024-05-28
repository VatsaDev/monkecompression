import os
import matplotlib.pyplot as plt
from collections import Counter

# Define the path to the folder and block length
folder_path = 'data'
block_length = 32  # You can change this to any block length you need

# Get the list of files in the folder
files = os.listdir(folder_path)
files.sort()

# Initialize counters
total_blocks = 0
ninety_percent_ones = 0
all_ones = 0
ninety_percent_zeros = 0
all_zeros = 0

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
                total_blocks += 1
                ones_count = block.count('1')
                zeros_count = block.count('0')
                
                if ones_count >= 0.9 * block_length:
                    ninety_percent_ones += 1
                if ones_count == block_length:
                    all_ones += 1
                if zeros_count >= 0.9 * block_length:
                    ninety_percent_zeros += 1
                if zeros_count == block_length:
                    all_zeros += 1
                    
    c += 1
    if c%100==0:
        print(c)

# Print the results
print(f'Total number of {block_length}-bit blocks: {total_blocks}')
print(f'Total number of blocks with at least 90% 1s: {ninety_percent_ones}')
print(f'Total number of blocks with all 1s: {all_ones}')
print(f'Total number of blocks with at least 90% 0s: {ninety_percent_zeros}')
print(f'Total number of blocks with all 0s: {all_zeros}')

# Optional: Plot the results
labels = ['90% 1s', 'All 1s', '90% 0s', 'All 0s']
values = [ninety_percent_ones, all_ones, ninety_percent_zeros, all_zeros]

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Block Type')
plt.ylabel('Count')
plt.title(f'Distribution of Specific {block_length}-bit Blocks')
plt.tight_layout()
plt.show()

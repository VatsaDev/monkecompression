from collections import Counter

def compress_binary_string(s):
    compressed = []
    i = 0
    length = len(s)
    
    while i < length:
        count = 1
        while i + 1 < length and s[i] == s[i + 1]:
            i += 1
            count += 1
        
        if count >= 7:
            compressed.append(f"({count}x{s[i]})")
        else:
            compressed.append(s[i] * count)
        
        i += 1
    
    return ''.join(compressed)

with open("C:\\Users\\vatsa\\Desktop\\projects\\monkeComp\\monke.txt", 'r') as f:
    file_contents = str(f.read())
    print(len(file_contents))
    compressed_string = compress_binary_string(file_contents)
    print(len(compressed_string))
    with open("C:\\Users\\vatsa\\Desktop\\projects\\monkeComp\\monkeC1.txt", 'w') as f1:
        f1.write(compressed_string)
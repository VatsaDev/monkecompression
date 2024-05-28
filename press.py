import os

# first wav
folder_path = 'data'
files = os.listdir(folder_path)
files.sort()

flens = []

c = 0

for file in files:
    first_file_path = os.path.join(folder_path, file)

    with open(first_file_path,'rb') as f:
        content = f.read()
        b_content = ''.join(format(byte, '08b') for byte in content)
        
        #flens.append(len(b_content))
        with open('C:\\Users\\vatsa\\Desktop\\projects\\monkeComp\\monke.txt','a') as f:
            f.write(b_content)
        
    c+=1
    
    if c%100==0:
        print(c)
        
#print(sum(flens)/len(flens))
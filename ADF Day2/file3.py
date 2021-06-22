import re
file=open("nivi2.txt","r")
# Lines = file.readlines()
for line in file:
    string = re.sub("[^a-zA-Z0-9]", " ",line)
    str=string.replace(" ","-")
print(str)

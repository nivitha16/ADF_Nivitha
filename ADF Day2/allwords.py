import re
list=[]
file=open("nivi2.txt","r")
Lines = file.readlines()
for line in Lines:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    for s1 in string:
        if s1 != "":
            list.append(s1)

print(list)

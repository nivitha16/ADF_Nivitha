import re
caps = []
file = open("nivi2.txt", "r")
Lines = file.readlines()
for line in Lines:
    string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
    for i in string:
        a = list(i)
        a[2::3] = [x.upper() for x in a[2::3]]
        i = ''.join(a)
        caps.append(i)
print(caps)
for line in Lines:
    string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
    for i in range(4, len(string), 5):
        string[i] = string[i].upper()
print(string)




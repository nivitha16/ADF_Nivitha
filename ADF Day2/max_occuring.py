import re
list1=[]
str1=""
freq=0
file=open("nivi2.txt","r")
for line in file:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    for s in string:
         if s != "":
            list1.append(s)

for i in list1:
    c=list1.count(i)
    if(c > freq):
        freq = c
        str1=i

print(str1)
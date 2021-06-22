import re

# initializing strings
vowels=""
list1=[]
file=open("nivi2.txt","r")
reader=file.readlines()
for line in reader:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    for s in string:
        if s!=0:
            list1.append(s)
    vowels=[re.sub("[aeiouAEIOU]","",i) for i in list1]
    for i in vowels:
        print(i,end=" ")


# printing result
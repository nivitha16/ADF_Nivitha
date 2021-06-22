import re
list=open("nivi2.txt", 'r')
list1=[]
for line in list:
     string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")
     for s1 in string:
         if(s1!=""):
          list1.append(s1)

for i in enumerate(list1):
    print (i)
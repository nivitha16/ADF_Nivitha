import re
file=open("nivi2.txt","r")
string = file.read()
input = string.replace('\n', ';')
print(input)
f2=open("newfile4.txt","w+")
f2.write(input)
f2.close()


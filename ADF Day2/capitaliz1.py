
import re
import string
str1=""
file=open("nivi2.txt","r")
for line in file:
    string1 = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    str1=str1+string
result = string.capwords(str1)
print(result)

# printing result
# print("The string after uppercasing Nth character : " + str(res))
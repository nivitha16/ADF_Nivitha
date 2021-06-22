import re
nivi=[]
file=open("nivi2.txt","r")
Lines = file.readlines()
for line in Lines:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    for s1 in string:
        if s1!="":
            if(s1.endswith("ing")):
                nivi.append(s1)
print(nivi)
# l = (sorted(list(nivi), key=len))
# l=list(sorted(nivi))
# with open('new2.txt', 'w') as f:
#     for items in l:
#         f.write('%s ' % items)
#     print("File written")
# f.close()
import re
nivi=set({})
file=open("nivi.txt","r")
Lines = file.readlines()
for line in Lines:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    for s1 in string:
        if s1!="":
          p=len(s1)
          nivi.add(str(p)+s1)
l = (sorted(list(nivi), key=len))
# l=list(sorted(nivi))
with open('new2.txt', 'w') as f:
    for items in l:
        f.write('%s ' % items)
    print("File written")
f.close()
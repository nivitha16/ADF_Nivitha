import re
i=0
file=open("nivi2.txt","r")
for line in file:
    string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
    list2=list(string)

list2 = list(dict.fromkeys(list2))
print(list2)

# l = (sorted(list(nivi), key=len))
# l=list(sorted(nivi))
# with open('new2.txt', 'w') as f:
#     for items in l:
#         f.write('%s ' % items)
#     print("File written")
# f.close()
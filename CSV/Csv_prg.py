import csv
try:
    f=open("records.csv","r")
    s1=csv.reader(f)
    details={}
    for row in s1:
        details[row[0]]={'state':row[1],'city':row[2]}

    print(details)
except:
    print("An exception occured")
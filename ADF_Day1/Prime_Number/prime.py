import time
try:
    i=2
    print("Prime Numbers are:")
    while 1:
        flag = 0
        for j in range(2,i):
           if (i%j)==0:
              flag=1
        if flag==0:
           print(i)
           time.sleep(5)
        i=i+1
except:
    print("An Exception occured")

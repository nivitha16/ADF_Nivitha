try:
    n1=int(input());
    n2=int(input());
    n3=abs(n1)
    n4=abs(n2)
    if(n3<n4):
        min=n3
    else:
        min=n4
    for i in range(1,min+1):
        if((n3%i==0) and (n4%i==0)):
            res=i
    if(n3==0):
        print(n4)
    elif(n4==0):
        print(n3)
    else:
        print(res)
except:
    print("An exception occured")

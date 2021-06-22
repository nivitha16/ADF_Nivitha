try:
    n1=int(input())
    bin=""
    while n1!=0:
        rem1=n1%2
        n1=n1//2
        bin=str(rem1)+bin
    print("The binary representation is",bin)

except:
    print("An exception occured")
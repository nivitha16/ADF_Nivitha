try:
    n3=int(input())
    hex=""
    list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while n3!=0:
        rem3=n3%16
        n3=n3//16
        hex = list[rem3] + hex
    print("The hexadecimal representation is",hex)

except:
    print("An exception occured")
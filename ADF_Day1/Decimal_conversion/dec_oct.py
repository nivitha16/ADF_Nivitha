try:
    n2=int(input())
    oct=""
    while n2!=0:
        rem2=n2%8
        n2=n2//8
        oct=str(rem2)+oct
    print("The octal representation is",oct)

except:
    print("An exception occured")
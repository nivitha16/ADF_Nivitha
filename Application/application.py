try:
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    gender=input("Enter Gender:")
    salary=input("Enter Salary:")
    state=input("Enter State:")
    city=input("Enter City:")

    print("USER CREDENTIALS")
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)
    print("Salary:",salary)
    print("State:",state)
    print("City:",city)
except:
    print("An Exception occured")

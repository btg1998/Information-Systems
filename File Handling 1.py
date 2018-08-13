fname=None
try:
    fname=input("Enter your First Name: ")
    if not fname:
        fname = None
        raise Exception("-_-")
    if not fname.isalpha():
        raise ValueError("First name should contain alphabets only.")
except ValueError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
lname=None
try:
    lname=input("Enter your Last Name: ")
    if not lname:
        lname = None
        raise Exception("-_-")
    if not lname.isalpha():
        raise ValueError("Last name should contain alphabets only.")
except ValueError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
name=fname+" "+lname
print("Name: ",name)

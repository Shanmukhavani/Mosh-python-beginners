name = input("Enter Name ")
if len(name) < 3:
    print("Name must be atleast 3 chars")
elif len(name) > 50 :
    print("Name can be maximum of 50 chars")
else:
    print("Name looks good")
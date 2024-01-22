#need to convert weight to required format
weight = int(input("Enter your weight "))
format = input ("(L)bs or (K)g ")
if format.upper() == 'L':
    print(f' you are {weight * 0.45} kgs ')
elif format.upper()=='K':
    print(f'You are {weight/0.45} lbs')
else:
    print("Choose correct option")
#Extracting characters in string
course = 'python for beginners'
print(course[0]) #prints first character
print(course[-1])#prints last character
print(course[-2])#prints second last character
print(course[0:3])#prints characters from 0 to 2 ,index 3 is excluded OUTPUT : pyt 
print(course[1:])#prints characters from 1 to end OUTPUT : ython for beginners 
print(course[:5])#prints characters from 0 to 4   OUTPUT: pytho 
print(course[:])#output :python for beginners

#copying variable
another = course[:]
print("another string is "+another)

print (course[1:-1]) #output: ython for beginner
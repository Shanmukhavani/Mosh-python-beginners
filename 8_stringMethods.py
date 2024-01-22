course = 'Python for Beginners'

# len()-gives length of the string.
print(len(course)) #20

#upper()

print(course.upper()) #PYTHON FOR BEGINNERS
print(course) #Python for Beginners (original string not changed)

 #lower()
print(course.lower()) #python for beginners



#find() -finding sequence of characters in the string
'''
find() -used to find the sequence of characters , it is a case sensitive function.If you pass char which is 
not present in the string then it always displays -1
'''
print(course.find('P')) #0 -gives index of the character
print(course.find('z')) #-1
print(course.find('p'))#-1

print(course.find('Beginner')) #11 -because the string Beginner is starting from the index 11

#replace() - REPLACES STRING -
'''
This method also case sensitive,if string to be replaced not found the string will remain
same
'''
print(course.replace('Beginner','Expert'))
print(course) #original string wont be affected
print(course.replace('beginner','Expert')) #Python for Beginners 
'''(nothing changed because beginner is not found,it is case sensitive)'''
print(course.replace('P','J')) #Jython for Beginners


'''in keyword'''  #To find the existance of the substrings in a string  

print('Python' in course) #True

'''Differnence between find and in'''
#find - returns the index whereas in- returns boolean value

#title() 
'''used to change the initial character in each word to Uppercase and the subsequent
   characters to Lowercase and then returns a new string.'''
print(course.title()) #Python For Beginners
#Formatted strings are useful in situations where you dynamically generate some text with your variables.
fName = 'John'
lName ='Smith'
#desired o/p is John [Smith] is a coder
message = fName +' ['+lName+'] is a coder'
#print(message)
 #but above way is not prefferable

msg = f'{fName} [{lName}] is a coder' #formatted strings are prefixed by f
print(msg)
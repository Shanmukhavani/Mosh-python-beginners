'''
The parameters are the positional arguments 
for ex:
def greet_user(first_name,sur_name):
    print(f'first name is  {first_name}')
    print(f'surname is {sur_name}')

greet_user("chintha","shanmukha")

output:
first name is  chintha
surname is shanmukha

here values are printed just based on the positions of arguments we are passing .
so we have foolowing alternative to avoid this issue.

'''
def greet_user(first_name,sur_name):
    print(f'first name is  {first_name}')
    print(f'surname is {sur_name}')

greet_user(sur_name="chintha",first_name="shanmukha")
greet_user("Samyuktha",sur_name="chintha")
#greet_user(sur_name="chintha","Samyuktha")-->gives error


'''
OUTPUT:
first name is  shanmukha
surname is chintha

NOTE : You should not pass normal positional arguments after keyarguments.it will pop error
Ex:greet_user(sur_name="chintha","Samyuktha")--->pops error
you can use keyarguments after positional arguments
'''
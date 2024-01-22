
#output:
#PS C:\Users\cvani\OneDrive\Desktop\python> python 38_Exceptions.py
#Age : 30
#30
#but if you give string as input you will get Value error.

#PS C:\Users\cvani\OneDrive\Desktop\python> python 38_Exceptions.py
#Age : asd
#Traceback (most recent call last):
 # File "C:\Users\cvani\OneDrive\Desktop\python\38_Exceptions.py", line 1, in <module>
  #  age = int(input("Age : "))
   #       ^^^^^^^^^^^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'asd'

#So we use Exceptions to solve this problem .


try:
    age = int(input("Age : "))
    income = int (input("Income : "))
    profit = income / age
    print(f'profit : {profit}')
    print(age)

except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid age")

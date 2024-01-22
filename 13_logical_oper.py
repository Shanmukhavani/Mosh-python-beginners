'''
and - loop gets executed only if all statements are true 
or - loop gets executed if atleast one statements is true 
not - inverses the boolean we give
'''
# and
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible for loan") #Eligible for loan
else:
    print("Not-Eligible for loan")

high_income2 = True
good_credit2 = False
if high_income2 and good_credit2:
    print("Eligible for loan")
else:
    print("Not-Eligible for loan") #Not-Eligible for loan


#or - excutes if atleast one statement is true
high_income3 = True
good_credit3= False
if high_income2 or good_credit2:
    print("Eligible for loan")
else:
    print("Not-Eligible for loan")
    
#not 
criminal_record = False
if high_income and not criminal_record:
    print("Yes ,Eligible for the program") #Yes ,Eligible for the program
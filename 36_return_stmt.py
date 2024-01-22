'''def square(num):
    return num*num
result = square(5)
print(result) #25
'''
'''case 2- if you remove return and print result directly in function and then after if u call function outside you
 will get result and then none its because by default function returns none
 Even if u cant write return it willautomatically write line like return None
 '''

def square(num):
    print(num*num)
    #return None --->python keeps this line by default.
print(square(5)) 

'''
output:
25
None
'''
'''
numbers = [5,2,5,2,2]
for number in numbers:
    print('X' * number)


OUTPUT:

XXXXX
XX
XXXXX
XX
XX

'''

numbers = [5,2,5,2,2]
for x in numbers:
    for y in range(x):
        print('X',end="")
    print()

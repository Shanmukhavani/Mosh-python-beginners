num = 9
i=1


while i<=3:
    guess = int(input('Guess the number'))
    i+=1
    if guess == num:
        print('You win')
        break
else:
    print('Sorry you failed!')

'''
just like if , while also have else in python but that else part only executes
if while loop completely executes by passing the conditions without any break
'''
#for loop is used to iterate over the string
for item in 'Python':
    print(item)
'''
output:
p
y
t
h
o
n
'''


for item in [1,2,3,4,5,6]:
    print(item)
'''
output:
1
2
3
4
5
6
'''
for item in range(10):
    print(item)
'''
output:
0
1
2
3
4
5
6
7
8
9
'''
for item in range(5,10):
    print(item)
'''
5
6
7
8
9
'''

#Adding step of 2
for item in range(5,10,2):
    print(f'{item} is started')
'''
output:
5 is started
7 is started
9 is started
'''
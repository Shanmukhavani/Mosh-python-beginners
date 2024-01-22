#unpacking is the powerful feature in python
'''
lets have an example 
coordinates = (1,2,3)
if we want to multiply we need to write this big code.
coordinate[0]*coordinate[1]*coordinate[2].but its a little bit too long.
so we can write it as
x=coordinate[0]
y=coordinate[1]
z=coordinate[2]
then we can write x*y*z
but this is also bit lengthy so we have another option called unpacking in python.
we can simply do them as follows
x,y,z = coordinates
so here first item 1 is assigned with x ,2 to y and 3 to z
this feature is not limited to only tuple we can add it with list also
'''
coordinates = (1,2,3)
x,y,z = coordinates
print(x) #1
print(y) #2
print(z) #3

#for lists
coordinates = [1,2,3]
x,y,z = coordinates
print(x) #1
print(y) #2
print(z) #3
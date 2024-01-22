# A constructor is an object that gets called during the creation of object of class.
class Point:
    def __init__(self,x,y): # self is used to reference the current object 
        self.x=x
        self.y=y 
    def draw(self):
        print("draw")
    def move(self):
        print("move")
point1 = Point(10,20)
print(point1.x) #10
point1.x=20
print(point1.x)#20

'''
using init you can initialize the object and we refer to this method as constructor.using this method 
we can construct or create an object.
'''
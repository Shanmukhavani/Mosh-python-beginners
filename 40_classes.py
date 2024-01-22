'''naming convention for classes is first letter of class should be capital.
Ex: Email , EmailClient
for variables and the fuctions it should be small and words are seperated by _
ex : email , email_client
'''
class Point :
    def draw(self):
        print ('draw')

    def move(self):
        print('move')


point1 = Point()
point1.draw()
#you can also set coordinates 
point1.x=10
point1.y=20
print(point1.x)
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hi!! I am {self.name}')
p1 = Person("Shanmukha")
print(p1.name)#Shanmukha
p1.talk() #Hi!! I am Shanmukha

p2 =Person("vani")
p2.talk()#Hi!! I am vani
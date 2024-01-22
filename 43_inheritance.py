class Mammal:
    def walk(self):
        print("Can walk")
class Dog(Mammal): #inheriting from mammal class by passing mammal class as an argument.
    def bark(self):
        print("Dogs can bark")
class Cat(Mammal):
    def annoying(self):
        print("Cats are annoying")

Dog1 = Dog()
Dog1.walk() #Can walk
Dog1.bark() #Dogs can bark

cat1 = Cat()
cat1.annoying() #Cats are annoying
cat1.walk()#Can walk

'''
if you dont have any methods in child class python gives error. so you just keep pass to get rid of that error
class Cat(Mammal):
   pass

'''
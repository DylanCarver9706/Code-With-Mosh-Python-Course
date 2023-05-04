class Mammal: # Parent class. Can pass down reusable functions
    def walk(self):
        print("walk")


class Dog(Mammal): # Defining parent class
    pass # pass this line to prevent empty class
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk() # method called from parent class
dog1.bark() # method called from created class

cat1 = Cat()
cat1.walk()
cat1.meow()
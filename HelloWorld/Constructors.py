class Point: # Pascal naming convention
    def __init__(self, x, y): #Constructor: Setting defailt values when object is initialized
        self.x = x # Setting x = to the x argument passed into function
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Dylan")
print(person.name)
person.talk()

bob = Person("Bob")
print(bob.name)
bob.talk()
class Point: # Pascal naming convention
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10 #attribute of the Point object
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
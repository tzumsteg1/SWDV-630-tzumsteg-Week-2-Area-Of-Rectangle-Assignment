import random

class Rectangle():
# allow the class to accept two variables -- a length and width
    def __init__(self, l, w):
        self.length = l
        self.width  = w

# area of a rectangle is simply length multiplied by the width
    def rectangle_area(self):
        return self.length*self.width
    
# I am using the random integer generator to create random sized rectangles with each run.
length = random.randint(1,20)
width = random.randint(1,20)

newRectangle = Rectangle(length, width)
print("length: ",length)
print("width: ",width)
print("Area: ",newRectangle.rectangle_area())
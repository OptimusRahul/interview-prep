"""
Design a class Rectangle with the following specifications :

Attributes :

length (double) : Represents the length of the rectangle
width (double) : Represents the width of the rectangle.
area (double) : Represents the area of rectangle.
Constructors :

A default constructor that initializes both length and width to 1.0
A parameterized constructor that takes two arguments to initialize length and width.
Methods :

void calculateArea() : Computes the area of rectangle.
void displayDetails() : Prints the rectangle's details, including its dimensions and area, in format specified below :


Refer the sample examples for understanding the output format.

Refer the commented code on IDE for output statements.
"""

class Rectangle:
    length: float
    width: float
    area: float

    def __init__(self, length: float = 1.0, width: float = 1.0):
        self.length = length
        self.width = width

    def calculateArea(self):
        self.area = self.length * self.width

    def displayDetails(self):
        print("Length : {:.2f}".format(self.length))
        print("Width : {:.2f}".format(self.width))
        print("Area : {:.2f}".format(self.area))

if __name__ == "__main__":

    # Create input for taking values from the user
    length = float(input())
    width = float(input())

    # Create first object of Rectangle class using the default constructor
    r1 = Rectangle()
    r1.calculateArea()
    r1.displayDetails()

    # Create second object of Rectangle class using the parameterized constructor
    r2 = Rectangle(length, width)
    r2.calculateArea()
    r2.displayDetails()
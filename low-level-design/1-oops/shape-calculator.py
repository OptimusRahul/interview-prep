"""
Design a class ShapeCalculator that calculates the area of different shapes using method overloading. Implement the below attributes and methods to calculate the area of different shapes :

Methods :

area (integer radius) : Calculates and print the area of circle using the formula π×radius2 .
area (integer length, integer width) : Calculates and print the area of rectangle using the formula (length * width).
area (integer base1, integer base2, integer height) : Calculates and print the area of Trapezoid using the formula ( (base1 + base2) * height) / 2.


Refer the sample examples for understanding the output format.

Refer the commented code for the output statements.

Consider π = 3.14



Note : Print the Area in integer format. Round down to nearest integer i.e. 3.9 should b 3, 2.1 should be 2.


Example 1

Input : radius = 2 , length = 2 , width = 3 , base1 = 2 , base2 = 3, height = 2

Output :

Area of Circle : 12

Area of Rectangle : 6

Area of Trapezoid : 5

Explanation :

We create the object of the class ShapeCalculator.
Calls the area method with radius as argument. It calculates and prints the area of circle.
Calls the area method with length and width as arguments. It calculates and prints the area of rectangle.
Calls the area method with base1, base2, height as arguments. It calculates and prints the area of trapezoid.
Example 2

Input : radius = 3 , length = 2 , width = 5 , base1 = 4 , base2 = 3, height = 5

Output :

Area of Circle : 28

Area of Rectangle : 10

Area of Trapezoid : 17

Explanation :

We create the object of the class ShapeCalculator.
Calls the area method with radius as argument. It calculates and prints the area of circle.
Calls the area method with length and width as arguments. It calculates and prints the area of rectangle.
Calls the area method with base1, base2, height as arguments. It calculates and prints the area of trapezoid.
"""

class ShapeCalculator:
    def area(self, *args):
        if len(args) == 1:
            radius = args[0]
            result = 3.14 * radius * radius
            print("Area of Circle : " + str(result))
        elif len(args) == 2:
            length, width = args
            result = length * width
            print("Area of Rectangle : " + str(result))
        elif len(args) == 3:
            base1, base2, height = args
            result = (base1 + base2) * height
            print("Area of Trapezoid : " + str(result))

def main():
    radius = int(input("Enter the radius of the circle: "))

    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    base1 = int(input("Enter the base1 of the trapezoid: "))
    base2 = int(input("Enter the base2 of the trapezoid: "))
    height = int(input("Enter the height of the trapezoid: "))

    sc = ShapeCalculator()
    sc.area(radius)
    sc.area(length, width)
    sc.area(base1, base2, height)

if __name__ == "__main__":
    main()

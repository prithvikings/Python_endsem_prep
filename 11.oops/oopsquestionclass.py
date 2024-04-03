"""create a class named "circle" which prints the area and perimeter of the circle also create the dervied class "airthemetic operations " 
which performs the addition subtraction and multiplication of two numbers"""

#we will use inheritence concept

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.1416 * (self.radius ** 2)
        return area

    def calculate_perimeter(self):
        perimeter = 2 * 3.1416 * self.radius
        return perimeter

# Derived class ArithmeticOperations without using math module
class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

# Example usage of Circle class
radius = int(input("Enter the radius: "))
circle_obj = Circle(radius)
area = circle_obj.calculate_area()
perimeter = circle_obj.calculate_perimeter()
print(f"Circle Area: {area:.2f}")
print(f"Circle Perimeter: {perimeter:.2f}")

# Example usage of ArithmeticOperations class
num1 = 10
num2 = 5
arithmetic_obj = ArithmeticOperations(num1, num2)
print(f"Addition: {arithmetic_obj.addition()}")
print(f"Subtraction: {arithmetic_obj.subtraction()}")
print(f"Multiplication: {arithmetic_obj.multiplication()}")

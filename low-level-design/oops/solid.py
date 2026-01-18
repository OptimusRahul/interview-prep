from abc import ABC, abstractmethod

# Single Responsibility Principle

class SalaryCalculator:
    def calculate_salary(self, hours_worked, hourly_rate):
        pass

class ReportGenerator:
    def generate_report(self, salary):
        pass

# Open/Closed Principle

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Liskov Substitution Principle

# Voilation of Liskov Substitution Principle
class Bird:
    def eat(self, name: str):
        print(f"{name} is eating")

class FlyingBird:
    def fly(self):
        print("Bird is flying")

class Eagle(Bird, FlyingBird):
    def fly(self):
        print("Eagle is flying")

class Penguin(Bird):
    pass


class Bird(ABC):
    def eat(self, name: str):
        print(f"{name} is eating")

class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Eagle(Bird,FlyingBird):
    def fly(self):
        print("Eagle is flying")

class Penguin(Bird):
    pass

# Interface Segregation Principle

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")
    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")

# Dependency Inversion Principle

class Keyboard(ABC):
    @abstractmethod
    def type(self):
        pass

class MechanicalKeyboard(Keyboard):
    def type(self):
        print("Mechanical keyboard is typing")

class WirelessKeyboard(Keyboard):
    def type(self):
        print("Wireless keyboard is typing")

class Computer:
    def __init__(self, keyboard: Keyboard):
        self.keyboard = keyboard
    
    def type(self):
        self.keyboard.type()

if __name__ == "__main__":
    eagle = Eagle()
    eagle.eat("Eagle")
    eagle.fly()
    penguin = Penguin()
    penguin.eat("Penguin")

    mechanicalKeyboard = MechanicalKeyboard()
    wirelessKeyboard = WirelessKeyboard()
    computer = Computer(mechanicalKeyboard)
    computer.type() 
    computer = Computer(wirelessKeyboard)
    computer.type()
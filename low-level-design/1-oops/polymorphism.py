class Calculator:
    def sum(self, a, b):
        return a + b

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof")
    
if __name__ == "__main__":
    # Compile time polymorphism
    calculator = Calculator()
    print(calculator.sum(1, 2))
    print(calculator.sum(1.0, 2.0))

    # Runtime polymorphism
    dog = Dog()
    dog.sound()


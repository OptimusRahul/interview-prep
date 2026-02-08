"""
You are required to design a program that utilizes an abstract class Animal to serve as the foundation for specific animal classes. The objective is to demonstrate runtime polymorphism where derived classes override the behaviour of the abstract method makeSound(). The program should include:

An abstract class Animal :

Attributes :

name (string) : Represents the name of the animal.
Abstract Method :

makeSound() : To print the sound specific to the animal.
Derived Classes :

Dog class : Inherits class Animal and overrides the makeSound() method to print "Woof!".
Cat class : Inherits class Animal and overrides the makeSound() method to print "Meow!".


Refer sample example to understand about the output format.

Refer the commented code on IDE to view the output statements.


Example 1

Input : d_name = "Buddy" , c_name = 'Whiskers"

Output :

The dog Buddy says : Woof!

The cat Whiskers says : Meow!

Explanation :

First the object of Dog class is created with the name provided for the dog.
Then the dog object is used to call the makeSound() method to print the output for the dog.
Now the object of Cat class is created with name provided for the cat.
Then the cat object is used to call the makeSound() method to print the output for the cat.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        print("The dog " + self.name + " says : Woof!")

class Cat(Animal):
    def makeSound(self):
        print("The cat " + self.name + " says : Meow!")

def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    dog.makeSound()
    cat.makeSound()

if __name__ == "__main__":
    main()

"""
This is the driver code that will execute and demonstrate the functionality of your abstract class `Animal` and the derived classes `Dog`, `Cat`.

First, the object of the class Dog is created along with the dog name.
Then the Dog class object is used to call the method makeSound() to print the corresponding text of Dog class.

Next, the object of the class Cat is created along with the cat name.
Then the Cat class object is used to call the method makeSound() to print the corresponding text of Cat class.


def main():
    # Input names for dog and cat
    dName = input()
    cName = input()

    # Create Dog object
    dog = Dog(dName)
    dog.makeSound()

    # Create Cat object
    cat = Cat(cName)
    cat.makeSound()


if __name__ == "__main__":
    main()
"""


"""
# Below are the output statements

print("The dog " + name + " says : Woof!")
print("The cat " + name + " says : Meow!")
"""
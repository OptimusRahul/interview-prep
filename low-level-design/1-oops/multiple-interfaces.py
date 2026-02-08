from abc import ABC, abstractmethod

class CarInterface(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @staticmethod
    def displayDetails():
        print("Car Details")


class CompanyInterface(ABC):
    @abstractmethod
    def getCompanyName(self):
        pass

class Car(CarInterface, CompanyInterface):
    def __init__(self, companyName: str):
        self.companyName = companyName

    def getCompanyName(self):
        return self.companyName

    def start(self):
        print("Company " + self.companyName + " is starting the car")

    def stop(self):
        print("Company " + self.companyName + " is stopping the car")

    def accelerate(self):
        print("Company " + self.companyName + " is accelerating the car")

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    @abstractmethod
    def walk(self):
        pass

class Human(Mammal):
    def eat(self):
        print("Human is eating")

    def walk(self):
        print("Human is walking")


def main():
    car = Car("Toyota")
    car.start()
    car.stop()
    car.accelerate()
    car.getCompanyName()
    CarInterface.displayDetails()

    human = Human()
    human.eat()
    human.walk()

if __name__ == "__main__":
    main()




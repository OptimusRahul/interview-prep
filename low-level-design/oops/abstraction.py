from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        print("Car initialized")

    @abstractmethod
    def start(self):
        pass

    # @abstractmethod
    # def airbags(self):
    #     pass

    @staticmethod
    def horn():
        print("Beep")

    def noise(self):
        print("Vroom")

class Engine(Car):
    def __init__(self):
        print("Engine initialized")
    @abstractmethod
    def isInternalCombustionEngine(self):
        pass

class ManualCar(Engine):
    def __init__(self):
        print("ManualCar initialized")

    def start(self):
        print("Start the car")

    def isInternalCombustionEngine(self):
        return True

    def displayDetails(self):
        print("Manual Car")

class AutomaticCar(Engine):
    def __init__(self):
        print("AutomaticCar initialized")
    def start(self):
        print("Start the car")

    def isInternalCombustionEngine(self):
        return False

    def displayDetails(self):
        print("Automatic Car")


def main():
    manualCar = ManualCar()
    manualCar.start()
    manualCar.noise()
    manualCar.horn()
    manualCar.displayDetails()

    # automaticCar = AutomaticCar()
    # automaticCar.start()
    # automaticCar.noise()
    # automaticCar.displayDetails()

if __name__ == "__main__":
    main()
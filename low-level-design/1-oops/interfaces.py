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

    def displayDetails(self):
        print("Car Details")
        
class ManualCar(CarInterface):
    def start(self):
        print("Start the car")

    def stop(self):
        print("Stop the car")

    def accelerate(self):
        print("Accelerate the car")
        

class AutomaticCar(CarInterface):
    pass

def main():
    manualCar = ManualCar()
    manualCar.start()
    manualCar.stop()
    manualCar.accelerate()
    manualCar.displayDetails()

if __name__ == "__main__":
    main()
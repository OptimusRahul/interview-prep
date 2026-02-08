from abc import ABC, abstractmethod
# Interface Segregation Principle

# Voilation of Interface Segregation Principle
class UberUser(ABC):
    @abstractmethod
    def bookRide(self):
        pass

    @abstractmethod
    def acceptRide(self):
        pass

    @abstractmethod
    def trackEarnings(self):
        pass

    @abstractmethod
    def ratePassenger(self):
        pass

    @abstractmethod
    def rateDriver(self):
        pass

class Rider(UberUser):
    def bookRide(self):  # yes
        pass

    def acceptRide(self):  # not needed
        pass

    def trackEarnings(self):  # not needed
        pass

    def ratePassenger(self):  # not needed
        pass

    def rateDriver(self):  # yes
        pass

class Driver(UberUser):
    def bookRide(self):  # not needed
        pass

    def acceptRide(self):  # yes
        pass

    def trackEarnings(self):  # yes
        pass

    def ratePassenger(self):  # not needed
        pass

    def rateDriver(self):  # not needed
        pass

# Solution for Interface Segregation Principle

class RiderInterface(ABC):
    @abstractmethod
    def bookRide(self):
        pass

    @abstractmethod
    def rateDriver(self):
        pass

class DriverInterface(ABC):
    @abstractmethod
    def acceptRide(self):
        pass

    @abstractmethod
    def trackEarnings(self):
        pass

    @abstractmethod
    def ratePassenger(self):
        pass


class RiderUser(RiderInterface):
    def bookRide(self):  # yes
        pass

    def rateDriver(self):  # yes
        pass

class DriverUser(DriverInterface):
    def acceptRide(self):  # yes
        pass

    def trackEarnings(self):  # yes
        pass

    def ratePassenger(self):  # yes
        pass

if __name__ == "__main__":
    riderUser = RiderUser()
    riderUser.bookRide()
    riderUser.rateDriver()

    driverUser = DriverUser()
    driverUser.acceptRide()
    driverUser.trackEarnings()
    driverUser.ratePassenger()
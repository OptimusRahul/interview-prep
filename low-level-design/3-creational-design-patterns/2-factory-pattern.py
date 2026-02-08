from abc import ABC, abstractmethod

# Bad Example
class Logistics(ABC):
    @abstractmethod
    def send(self):
        pass

class Road(Logistics):
    def send(self):
        print("Sending by road logic")

class Air(Logistics):
    def send(self):
        print("Sending by air logic")

class LogisticsService:
    def send(self, mode):
        if mode == "road":
            logistics = Road()
            logistics.send()
        elif mode == "air":
            logistics = Air()
            logistics.send()
        else:
            raise ValueError(f"Invalid mode: {mode}")

# Good Example
class Logistics(ABC):
    @abstractmethod
    def send(self):
        pass

class Road(Logistics):
    def send(self):
        print("Sending by road logic")

class Air(Logistics):
    def send(self):
        print("Sending by air logic")

class LogisticsFactory:
    @staticmethod
    def get_logistics(mode):
        if mode == "road":
            return Road()
        elif mode == "air":
            return Air()
        else:
            raise ValueError(f"Invalid mode: {mode}")

class LogisticsService:
    def send(self, mode):
        logistics = LogisticsFactory.getLogistics(mode)
        logistics.send()
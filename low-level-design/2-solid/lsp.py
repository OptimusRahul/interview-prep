# Liskov Substitution Principle

# Voilation of Liskov Substitution Principle
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def setWidth(self, width):
#         self.width = width

#     def setHeight(self, height):
#         self.height = height

#     def getArea(self):
#         return self.width * self.height

# class Square(Rectangle):
#     def __init__(self, width):
#         self.width = width
#         self.height = width

#     def setWidth(self, width):
#         self.width = width
#         self.height = width

#     def setHeight(self, height):
#         self.height = height
#         self.width = height

# def printArea(r):
#     r.setWidth(5)
#     r.setHeight(10)
#     print(r.getArea())

# if __name__ == "__main__":
#     rectangle = Rectangle(10, 5)
#     printArea(rectangle)

#     square = Square(5)
#     printArea(square)

# Corrected Solution for Liskov Substitution Principle
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def getArea(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, width):
        super().__init__(width, width)

    def getArea(self):
        return self.width * self.width


def printArea(r):
    r.setWidth(5)
    r.setHeight(10)
    print(r.getArea())

if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    printArea(rectangle)

    square = Square(5)
    printArea(square)

# Notification System
class Notification:
    # method implementing send notification functionality 
    def sendNotification(self):
        print("Notification sent")


# Email Notification class
class EmailNotification(Notification):
    def sendNotification(self):
        print("Email Notification sent")

# SMS Notification class
class SMSNotification(Notification):
    def sendNotification(self):
        print("SMS Notification sent")

# Push Notification class
class PushNotification(Notification):
    def sendNotification(self):
        print("Push Notification sent")

# Main class
if __name__ == "__main__":
    # Creating an object of Notification class
    notification = EmailNotification()

    # Working code on the notification object
    notification.sendNotification()

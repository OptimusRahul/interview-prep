"""
You are tasked with designing a Robot class to demonstrate the functionality of different types of inner classes, Implement the following:

Class Robot :

Attribute : name (string)

Method : performAction() - Prints the robot's action


Class Arm (Non-static Inner Class) :

Method: pickItem() to print the message "Arm picking an item.".


Class Processor (Static Nested Class) :

Method: process() to print the message "Processor analyzing the data.".

Local Inner Class : manageSensors() method is used to implement the local inner class sensor.

Method: sense() to print the message "Sensor detecting obstacles." which is defined inside the local inner class.


Anonymous Inner Class:

Implements an interface Task with a single method execute();

Method: executeTask() method to implement the overrides of execute() method of interface to print "Executing a custom task"



Refer the Commented code on IDE to see the output statements.
"""

from abc import ABC, abstractmethod

class Robot:
    def __init__(self, name: str):
        self.name = name

    def performAction(self):
        print(f"{self.name} is performing an action.")

    # Non-static inner class (simulated in Python by passing outer instance)
    class Arm:
        def __init__(self, outer_instance):
            self.outer = outer_instance

        def pickItem(self):
            print(f"{self.outer.name} arm picking an item.")

    # Static nested class
    class Processor:
        def process(self):
            print("Processor analyzing the data.")

    # Method demonstrating a local inner class
    def manageSensors(self):
        # Local inner class defined inside a method
        class Sensor:
            def __init__(self, outer_instance):
                self.outer = outer_instance

            def sense(self):
                print(f"{self.outer.name} sensor detecting obstacles.")

        sensor = Sensor(self)
        sensor.sense()

    # Interface (using ABC in Python)
    class Task(ABC):
        @abstractmethod
        def execute(self):
            pass

    # Anonymous inner class (simulated using a regular class instantiation)
    def executeTask(self):
        # Create an anonymous class by defining and instantiating immediately
        class AnonymousTask(Robot.Task):
            def __init__(self, outer_instance):
                self.outer = outer_instance

            def execute(self):
                print(f"{self.outer.name} executing a custom task.")

        task = AnonymousTask(self)
        task.execute()


def main():
    # Hardcoded input
    name = "Robot-1"

    # Create Robot object
    robot = Robot(name)

    # Call methods to demonstrate the inner classes and task
    robot.performAction()

    # Non-static inner class - needs outer instance
    arm = Robot.Arm(robot)
    arm.pickItem()

    # Static nested class - no outer instance needed
    processor = Robot.Processor()
    processor.process()

    # Local inner class
    robot.manageSensors()

    # Anonymous inner class
    robot.executeTask()


if __name__ == "__main__":
    main()

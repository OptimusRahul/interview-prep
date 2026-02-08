from abc import ABC, abstractmethod
# Static Inner Class
# class OuterClass:
#     staticVar: int = 100

#     class InnerClass:
#         def display(self):
#             print("Static variable:", OuterClass.staticVar)

# Non-Static Inner Class
# class OuterClass:
#     def __init__(self):
#         self.instanceVar = 10

#     class InnerClass:
#         def __init__(self, outer):
#             self.outer = outer

#         def display(self):
#             # Throws error because instanceVar is not static
#             # print("Instance variable:", OuterClass.instanceVar)
#             print("Instance variable:", self.outer.instanceVar)

# Local inner class
class OuterClass:
    def outerMethod(self):
        localVar = 10

        class LocalInnerClass:
            def __init__(self, value):
                self.localVarCopy = value

            def display(self):
                print("Local variable:", self.localVarCopy)

        localObj = LocalInnerClass(localVar)
        localObj.display()

# Anonymous inner class
class Greeting(ABC):
    @abstractmethod
    def greet(self):
        pass

if __name__ == "__main__":
    # Static Inner Class
    # outer = OuterClass.StaticNestedClass()
    # outer.display()  # Output: Static variable: 100

    # Non-Static Inner Class
    # outer = OuterClass()
    # inner = OuterClass.InnerClass(outer)
    # inner.display()

    # Local Inner Class
    outer = OuterClass()
    outer.outerMethod()

    class GreetingImpl(Greeting):
        def greet(self):
            print("Hello")

    greeting = GreetingImpl()
    greeting.greet()
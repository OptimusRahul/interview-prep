class Counter:
    count: int = 0

    def __init__(self):
        Counter.count += 1
    
    @staticmethod
    def displayCount():
        print("Count:", Counter.count)

class MathUtils:
    @staticmethod
    def add(a: int, b: int):
        return a + b

class Example:
    value: int = 0
    print("Static block executed")

class StaticNonStaticAccess:
    def __init__(self) -> None:
        self.instaceVar = 10

    @staticmethod
    def staticMethod():
        obj = StaticNonStaticAccess
        print("Static method called")
        print("Instance variable:", obj.instaceVar)

if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    Counter.displayCount()

    result = MathUtils.add(1, 2)
    print("Result:", result)

    print("Example value:", Example.value)
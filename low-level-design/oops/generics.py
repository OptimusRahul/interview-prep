from typing import List, Generic, TypeVar, Any, Sequence

# Generic type variable
T = TypeVar('T')

class GenericClass(Generic[T]):
    def __init__(self, obj: T):
        self.obj = obj

    def display(self) -> None:
        print("Type:", type(self.obj).__name__)

class Driver:
    @staticmethod
    def main() -> None:
        intObj = GenericClass[int](10)
        strObj = GenericClass[str]("Hello")
        intObj.display()
        strObj.display()

# Generic class
class Main:
    @staticmethod
    def main() -> None:
        list: List[str] = []
        list.append("Hello")
        # list.append(2000)

        str_val = list[0]
        print(str_val)

# Generic type variable
class Box(Generic[T]):
    def __init__(self):
        self.value: T | None = None

    def set(self, value: T) -> None:
        self.value = value

    def get(self) -> T | None:
        return self.value

# Generic method
class GenericMethodExample:
    def print(self, value: T) -> None:
        print("Data : ", value)
    

# Bound Type Parameter
class Number:
    def doubleValue(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError
    
class Integer(Number):
    def __init__(self, value):
        self.value = value

    def doubleValue(self):
        return self.value * 2

    def get_value(self):
        return self.value

    def print(self):
        print(self.value, end=" ")
    
class Double(Number):
    def __init__(self, value):
        self.value = value

    def doubleValue(self):
        return self.value * 2

    def get_value(self):
        return self.value

    def print(self):
        print(self.value, end=" ")

# Bounded type variable - T must be a Number or its subclass
N = TypeVar('N', bound=Number)

class NumericBox(Generic[N]):
    def __init__(self, num: N):
        self.num = num

    def square(self):
        return self.num.doubleValue() * self.num.doubleValue()

class UpperBoundExample:
    @staticmethod
    def printList(list: Sequence[Number]) -> None:
        for num in list:
            print(num.get_value(), end=" ")
        print()
    
class LowerBoundExample:
    @staticmethod
    def addNumbers(list: List[Any]) -> None:
        list.append(Integer(1))
        list.append(Integer(2))
        
        for num in list:
            if hasattr(num, 'print'):
                num.print()
        print()


Main.main()
Driver.main()

if __name__ == "__main__":
    intBox = Box[int]()
    intBox.set(100)
    print(intBox.get())

    strBox = Box[str]()
    strBox.set("Hello")
    print(strBox.get())

    obj = GenericMethodExample()
    obj.print(100)
    obj.print("Hello")

    intNumBox = NumericBox[Integer](Integer(10))
    print(intNumBox.square())

    doubleBox = NumericBox[Double](Double(10.5))
    print(doubleBox.square())

    # strBox = NumericBox("Hello")
    # print(strBox.square())

    intList = [Integer(1), Integer(2), Integer(3)]
    doubleList = [Double(1.1), Double(2.2), Double(3.3)]

    ub = UpperBoundExample()
    ub.printList(intList)
    ub.printList(doubleList)

    lb = LowerBoundExample()

    numList: List[Any] = []
    lb.addNumbers(numList)

    objList: List[Any] = []
    lb.addNumbers(objList)

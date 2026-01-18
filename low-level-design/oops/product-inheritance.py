class Product:
    __name: str
    __category: str
    __price: float

    def __init__(self, name: str, category: str, price: float):
        self.__name = name
        self.__category = category
        self.__price = price

    def displayDetails(self):
        print("Name : " + self.__name)
        print("Category : " + self.__category)
        print("Price : {:.2f}".format(self.__price))

class Electronics(Product):
    __warranty: int
    __brand: str

    def __init__(self, name: str, price: float, warranty: int, brand: str):
        super().__init__(name, "Electronics", price)
        self.__warranty = warranty
        self.__brand = brand

    def displayDetails(self):
        super().displayDetails()
        print("Warranty : " + str(self.__warranty))
        print("Brand : " + self.__brand)

class Clothing(Product):
    __size: str
    __color: str

    def __init__(self, name: str, price: float, size: str, color: str):
        super().__init__(name, "Clothing", price)
        self.__size = size
        self.__color = color

    def displayDetails(self):
        super().displayDetails()
        print("Size : " + self.__size)
        print("Color : " + self.__color)


class Main():
    def main(self):
        electronics = Electronics("Laptop", 1000.0, 2, "Dell")
        electronics.displayDetails()
        clothing = Clothing("Shirt", 100.0, "M", "Red")
        clothing.displayDetails()

if __name__ == "__main__":
    main = Main()
    main.main()
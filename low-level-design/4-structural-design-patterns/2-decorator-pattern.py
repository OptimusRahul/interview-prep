# BAD EXAMPLE
# Each combination of pizza requires a new class
class PlainPizza:
    pass

class CheesePizza(PlainPizza):
    pass

class OlivePizza(PlainPizza):
    pass

class StuffedPizza(PlainPizza):
    pass

class CheeseStuffedPizza(CheesePizza):
    pass

class CheeseOlivePizza(CheesePizza):
    pass

class CheeseOliveStuffedPizza(CheeseOlivePizza):
    pass

# GOOD EXAMPLE  
from abc import ABC, abstractmethod

# =========== Component Interface ============
class Pizza(ABC):
    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass


# ============= Concrete Components: Base pizza ==============
class PlainPizza(Pizza):
    def getDescription(self):
        return "Plain Pizza"

    def getCost(self):
        return 150.00


class MargheritaPizza(Pizza):
    def getDescription(self):
        return "Margherita Pizza"

    def getCost(self):
        return 200.00


# ======================== Abstract Decorator ===========================
# ====== Implements Pizza and holds a reference to a Pizza object =======
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza


# ============ Concrete Decorator: Adds Extra Cheese ================
class ExtraCheese(PizzaDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Extra Cheese"

    def getCost(self):
        return self.pizza.getCost() + 40.0


# ============ Concrete Decorator: Adds Olives ================
class Olives(PizzaDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Olives"

    def getCost(self):
        return self.pizza.getCost() + 30.0


# ============ Concrete Decorator: Adds Stuffed Crust Cheese ================
class StuffedCrust(PizzaDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Stuffed Crust"

    def getCost(self):
        return self.pizza.getCost() + 50.0



if __name__ == "__main__":
    # BAD: Using PlainPizza and decorators to create a pizza
    plainPizza = PlainPizza()

    # Pizzas with individual toppings
    cheesePizza = CheesePizza()
    olivePizza = OlivePizza()
    stuffedPizza = StuffedPizza()

    # Combinations of toppings require separate classes
    cheeseStuffedPizza = CheeseStuffedPizza()
    cheeseOlivePizza = CheeseOlivePizza()

    # Further combinations increase complexity exponentially
    cheeseOliveStuffedPizza = CheeseOliveStuffedPizza()

    # GOOD: Using decorators to create a pizza
    # Start with a basic Margherita Pizza
    myPizza = MargheritaPizza()

    # Add Extra Cheese
    myPizza = ExtraCheese(myPizza)

    # Add Olives
    myPizza = Olives(myPizza)

    # Add Stuffed Crust
    myPizza = StuffedCrust(myPizza)

    # Final Description and Cost
    print("Pizza Description:", myPizza.getDescription())
    print("Total Cost: ₹" + str(myPizza.getCost()))



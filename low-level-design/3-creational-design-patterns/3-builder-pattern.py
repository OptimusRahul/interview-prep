# Bad Example
# Represents a customizable Burger Meal
class BurgerMeal:
    # Constructor trying to handle all combinations
    def __init__(self, bun, patty, sides=None, toppings=None, cheese=False):
        # Mandatory components
        self.bun = bun
        self.patty = patty

        # Optional components
        self.sides = sides
        self.toppings = toppings
        self.cheese = cheese

# Constructing the object with only required details
burger_meal = BurgerMeal("wheat", "veg", None, None, False)

# Represents a customizable Burger Meal
class BurgerMealBuidler:
    # Private constructor to force use of Builder
    def __init__(self, builder):
        # Required components
        self.bunType = builder.bunType
        self.patty = builder.patty

        # Optional components
        self.hasCheese = builder.hasCheese
        self.toppings = builder.toppings
        self.side = builder.side
        self.drink = builder.drink

    # Static nested Builder class
    class BurgerBuilder:
        # Builder constructor with required fields
        def __init__(self, bunType, patty):
            # Required
            self.bunType = bunType
            self.patty = patty

            # Optional
            self.hasCheese = False
            self.toppings = []
            self.side = None
            self.drink = None

        # Method to set cheese
        def withCheese(self, hasCheese):
            self.hasCheese = hasCheese
            return self

        # Method to set toppings
        def withToppings(self, toppings):
            self.toppings = toppings
            return self

        # Method to set side
        def withSide(self, side):
            self.side = side
            return self

        # Method to set drink
        def withDrink(self, drink):
            self.drink = drink
            return self

        # Final build method
        def build(self):
            return BurgerMeal(self)

# Creating burger with only required fields
plain_burger = BurgerMealBuidler.BurgerBuilder("wheat", "veg").build()

# Burger with cheese only
burger_with_cheese = (
    BurgerMealBuidler.BurgerBuilder("wheat", "veg")
    .withCheese(True)
    .build()
)

# Fully loaded burger
toppings = ["lettuce", "onion", "jalapeno"]
loaded_burger = (
    BurgerMealBuidler.BurgerBuilder("multigrain", "chicken")
    .withCheese(True)
    .withToppings(toppings)
    .withSide("fries")
    .withDrink("coke")
    .build()
)

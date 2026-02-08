import java.util.*;

class BurgerMeal {
    private String bun;
    private String patty;

    private String sides;
    private List<String> toppings;
    private boolean cheese;

    public BurgerMeal(String bun, String patty, String sides, List<String> toppings, boolean cheese) {
        this.bun = bun;
        this.patty = patty;
        this.sides = sides;
        this.toppings = toppings;
        this.cheese = cheese;
    }

    // Telescoping Constructor Pattern
    // public BurgerMeal(String bun, String patty, boolean cheese) {}
    // public BurgerMeal(String bun, String patty, String sides, boolean cheese) {}
}

# Builder Pattern
class BurgerMealBuilder {
    // Required Parameters
    private final String bunType;
    private final String patty;

    // Optional Parameters
    private final boolean hasCheese;
    private final List<String> toppings;
    private final String side;
    private final String drink;

    private BurgerMealBuilder(BurgerBuilder builder) {
        this.bunType = builder.bunType;
        this.patty = builder.patty;
        this.hasCheese = builder.hasCheese;
        this.toppings = builder.toppings;
        this.side = builder.side;
        this.drink = builder.drink;
    }

    public static class BurgerBuilder {
        // Required Parameters
        private final String bunType;
        private final String patty;

        // Optional Parameters
        private final boolean hasCheese;
        private final List<String> toppings;
        private final String side;
        private final String drink;
        
        public BurgerBuilder(String bunType, String patty) {
            this.bunType = bunType;
            this.patty = patty;
        }

        public BurgerBuilder withCheese(boolean hasCheese) {
            this.hasCheese = hasCheese;
            return this;
        }

        public BurgerBuilder withToppings(List<String> toppings) {
            this.toppings = toppings;
            return this;
        }

        public BurgerBuilder withSide(String side) {
            this.side = side;
            return this;
        }

        public BurgerBuilder withDrink(String drink) {
            this.drink = drink;
            return this;
        }

        public BurgerMealBuilder build() {
            return new BurgerMealBuilder(this);
        }
    }
}

class Main {
    public static void main(String[] args) {
        BurgerMeal burgerMeal = new BurgerMeal("Sesame Bun", "Beef Patty", null, null, false);

        BurgerMealBuilder plainBurger = new BurgerMealBuilder.BurgerBuilder("wheat", "veg").build();
        BurgerMealBuilder cheeseBurger = new BurgerMealBuilder.BurgerBuilder("wheat", "beef").withCheese(true).build();
        BurgerMealBuilder deluxeBurger = new BurgerMealBuilder.BurgerBuilder("wheat", "beef").withCheese(true).withToppings(Arrays.asList("lettuce", "tomato", "onion")).withSide("fries").withDrink("coke").build();
    }
}
import java.util.*;

// BAD EXAMPLE
// Each combination of pizza requires a new class
class PlainPizza {}
class CheesePizza extends PlainPizza {}
class OlivePizza extends PlainPizza {}
class StuffedPizza extends PlainPizza {}
class CheeseStuffedPizza extends CheesePizza {}
class CheeseOlivePizza extends CheesePizza {}
class CheeseOliveStuffedPizza extends CheeseOlivePizza {}

// public class Main {
//     public static void main(String[] args) {
//         // Base pizza
//         PlainPizza plainPizza = new PlainPizza();

//         // Pizzas with individual toppings
//         CheesePizza cheesePizza = new CheesePizza();
//         OlivePizza olivePizza = new OlivePizza();
//         StuffedPizza stuffedPizza = new StuffedPizza();

//         // Combinations of toppings require separate classes
//         CheeseStuffedPizza cheeseStuffedPizza = new CheeseStuffedPizza();
//         CheeseOlivePizza cheeseOlivePizza = new CheeseOlivePizza();

//         // Further combinations increase complexity exponentially
//         CheeseOliveStuffedPizza cheeseOliveStuffedPizza = new CheeseOliveStuffedPizza();

//     }
// }


// GOOD EXAMPLE
interface Pizza {
    String getDescription();
    double getCost();
}

class PlainPizzaGood implements Pizza {
    @Override
    public String getDescription() {
        return "Plain Pizza";
    }

    @Override
    public double getCost() {
        return 150.00;
    }
}

class MargheritaPizza implements Pizza {
    @Override
    public String getDescription() {
        return "Margherita Pizza";
    }

    @Override
    public double getCost() {
        return 200.00;
    }
}

// Abstract Decorator
// Implements Pizza and holds a reference to a Pizza object
abstract class PizzaDecorator implements Pizza {
    protected Pizza pizza;

    public PizzaDecorator(Pizza pizza) {
        this.pizza = pizza;
    }
}

// Concrete Decorators
class ExtraCheese extends PizzaDecorator {
    public ExtraCheese(Pizza pizza) {
        super(pizza);
    }

    @Override
    public String getDescription() {
        return pizza.getDescription() + ", Extra Cheese";
    }

    @Override
    public double getCost() {
        return pizza.getCost() + 30.00;
    }
}

class Olives extends PizzaDecorator {
    public Olives(Pizza pizza) {
        super(pizza);
    }

    @Override
    public String getDescription() {
        return pizza.getDescription() + ", Olives";
    }

    @Override
    public double getCost() {
        return pizza.getCost() + 20.00;
    }
}

class StuffedCrust extends PizzaDecorator {
    public StuffedCrust(Pizza pizza) {
        super(pizza);
    }

    @Override
    public String getDescription() {
        return pizza.getDescription() + ", Stuffed Crust";
    }

    @Override
    public double getCost() {
        return pizza.getCost() + 50.0;
    }
}

public class Main {
    public static void main(String[] args) {

        // BAD: Using PlainPizzaGood and decorators to create a pizza
        // Each combination of pizza requires a new class
        // Base pizza
        PlainPizza plainPizza = new PlainPizza();

        // Pizzas with individual toppings
        CheesePizza cheesePizza = new CheesePizza();
        OlivePizza olivePizza = new OlivePizza();
        StuffedPizza stuffedPizza = new StuffedPizza();

        // Combinations of toppings require separate classes
        CheeseStuffedPizza cheeseStuffedPizza = new CheeseStuffedPizza();
        CheeseOlivePizza cheeseOlivePizza = new CheeseOlivePizza();

        // Further combinations increase complexity exponentially
        CheeseOliveStuffedPizza cheeseOliveStuffedPizza = new CheeseOliveStuffedPizza();

        // GOOD: Using decorators to create a pizza
        Pizza pizza = new PlainPizzaGood();
        pizza = new ExtraCheese(pizza);
        pizza = new Olives(pizza);
        pizza = new StuffedCrust(pizza);

        System.out.println(pizza.getDescription());
        System.out.println(pizza.getCost());
    }
}
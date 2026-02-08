import java.util.*;

interface Item {
    void accept(ItemVisitor visitor);
}

class PhysicalProduct implements Item {
    String name;
    double price;

    public PhysicalProduct(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public void accept(ItemVisitor visitor) {
        visitor.visit(this);
    }
}

class DigitalProduct implements Item {
    String name;
    int downloadSizeInMB;

    public DigitalProduct(String name, int downloadSizeInMB) {
        this.name = name;
        this.downloadSizeInMB = downloadSizeInMB;
    }

    public void accept(ItemVisitor visitor) {
        visitor.visit(this);
    }
}

class GiftCard implements Item {
    String name;
    double value;

    public GiftCard(String name, double value) {
        this.name = name;
        this.value = value;
    }

    public void accept(ItemVisitor visitor) {
        visitor.visit(this);
    }
}

interface ItemVisitor {
    void visit(PhysicalProduct product);
    void visit(DigitalProduct product);
    void visit(GiftCard product);
}

class InvoiceVisitor implements ItemVisitor {
    public void visit(PhysicalProduct product) {
        System.out.println("Printing invoice for Physical Product: " + product.name);
    }

    public void visit(DigitalProduct product) {
        System.out.println("Printing invoice for Digital Product: " + product.name);
    }

    public void visit(GiftCard product) {
        System.out.println("Printing invoice for Gift Card: " + product.name);
    }
}

class ShippingCostVisitor implements ItemVisitor {
    public void visit(PhysicalProduct product) {
        System.out.println("Calculating shipping cost for Physical Product: " + product.name);
    }

    public void visit(DigitalProduct product) {
        System.out.println("No shipping cost for digital product.");
    }

    public void visit(GiftCard product) {
        System.out.println("No shipping cost for gift card.");
    }
}

class Main {
    public static void main(String[] args) {
        List<Item> cart = new ArrayList<>();
        cart.add(new PhysicalProduct("Book", 100));
        cart.add(new DigitalProduct("Movie", 1000));
        cart.add(new GiftCard("Gift Card", 100));

        ItemVisitor invoiceVisitor = new InvoiceVisitor();
        ItemVisitor shippingCostVisitor = new ShippingCostVisitor();

        for(Item item : cart) {
            item.accept(invoiceVisitor);
            item.accept(shippingCostVisitor);

            System.out.println("");
        }
    }
}
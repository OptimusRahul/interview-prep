import java.util.*;

class PhysicalProduct {
    void printInvoice() {
        System.out.println("Printing invoice for phyiscal product");
    }

    double calculateShippingCost() {
        System.out.println("Calculating shipping cost for Physical Product...");
        return 10.00;
    }
}

class DigitalProduct {
    void printInvoice() {
        System.out.println("Printing invoice for digital product");
    }
}

class GiftCard {
    void printInvoice() {
        System.out.println("Printing invoice for Gift Card");
    }

    double calculateDiscount() {
        System.out.println("Calculating discount for Gift Card...");
        return 15.00;
    }
}

class Main {
    public static void main(String[] args) {
        List<Object> cart = Arrays.asList(new PhysicalProduct(), new DigitalProduct(), new GiftCard());

        for(Object item : cart) {
            if(item instanceof PhysicalProduct) {
                PhysicalProduct physicalProduct = (PhysicalProduct) item;
                physicalProduct.printInvoice();
                double shippingCost = physicalProduct.calculateShippingCost();
                System.out.println("Shipping Cost: " + shippingCost);
            } else if(item instanceof DigitalProduct) {
                DigitalProduct digitalProduct = (DigitalProduct) item;
                digitalProduct.printInvoice();
                System.out.println("No shipping cost for digital product.");
            } else if(item instanceof GiftCard) {
                GiftCard giftCard = (GiftCard) item;
                giftCard.printInvoice();
                double discount = giftCard.calculateDiscount();
                System.out.println("Discount: " + discount);
            }
        }
    }
}
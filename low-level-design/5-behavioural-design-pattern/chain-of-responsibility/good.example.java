import java.util.*;

abstract class SupportHandler {
    protected SupportHandler nextHandler;

    public void setNextHandler(SupportHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public abstract void handleRequest(String requestType);
}

class GeneralSupport extends SupportHandler {
    @Override
    public void handleRequest(String requestType) {
        if(requestType.equals("general")) {
            System.out.println("General support handler handles the request");
        } else if(nextHandler != null) {
            nextHandler.handleRequest(requestType);
        }
    }
}

class BillingSupport extends SupportHandler {
    public void handleRequest(String requestType) {
        if (requestType.equalsIgnoreCase("refund")) {
            System.out.println("BillingSupport: Handling refund request");
        } else if (nextHandler != null) {
            nextHandler.handleRequest(requestType);
        }
    }
}

class TechnicalSupport extends SupportHandler {
    @Override
    public void handleRequest(String requestType) {
        if(requestType.equals("technical")) {
            System.out.println("Technical support handler handles the request");
        } else if(nextHandler != null) {
            nextHandler.handleRequest(requestType);
        }
    }
}

class DeliverySupport extends SupportHandler {
    @Override
    public void handleRequest(String requestType) {
        if(requestType.equals("delivery")) {
            System.out.println("Delivery support handler handles the request");
        } else if(nextHandler != null) {
            nextHandler.handleRequest(requestType);
        } else {
            System.out.println("No handler available");
        }
    }
}

class Main {
    public static void main(String[] args) {
        SupportHandler general = new GeneralSupport();
        SupportHandler billing = new BillingSupport();
        SupportHandler technical = new TechnicalSupport();
        SupportHandler delivery = new DeliverySupport();

        // Setting up the chain: general -> billing -> technical -> delivery
        general.setNextHandler(billing);
        billing.setNextHandler(technical);
        technical.setNextHandler(delivery);

        // Testing the chain of responsibility with different request types
        general.handleRequest("refund");
        general.handleRequest("delivery");
        general.handleRequest("unknown");
    }
}
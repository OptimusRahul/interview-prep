// Bad Example
import java.util.*;

// Targer Interface:
// Standad interface expected by CheckoutService
interface PaymentGateway {
    void pay(String orderId, double amount);
}

// Concrete implementation of PaymentGateway for PayU
class PayUGateway implements PaymentGateway {
    @Override
    public void pay(String orderId, double amount) {
        System.out.println("Paid Rs. " + amount + " using PayU for order: " + orderId);
    }
}

// Adaptee:
// An existing class with an incompatible interface
class RazorpayAPI {
    public void makePayment(String invoiceId, double amountInRupees) {
        System.out.println("Paid Rs. " + amountInRupees + " using Razorpay for invoice: " + invoiceId);
    }
}

// Client Class:
// Uses PaymentGateway interface to process payments
class CheckoutService {
    private PaymentGateway paymentGateway;

    public CheckoutService(PaymentGateway paymentGateway) {
        this.paymentGateway = paymentGateway;
    }

    public void checkout(String orderId, double amount) {
        paymentGateway.pay(orderId, amount);
    }
}

class Main {
    public static void main(String[] args) {
        CheckoutService checkoutService = new CheckoutService(new PayUGateway());
        checkoutService.checkout("12", 2000);
    }
}

// Good Example
interface PaymentGatewayGood {
    void pay(String orderId, double amount);
}

// Concrete implementation of PaymentGatewayGood for PayU
class PayUGatewayGood implements PaymentGatewayGood {
    @Override
    public void pay(String orderId, double amount) {
        System.out.println("Paid Rs. " + amount + " using PayU for order: " + orderId);
    }
}

// Adaptee:
// An existing class with an incompatible interface
class RazorpayAPIGood {
    public void makePayment(String invoiceId, double amountInRupees) {
        System.out.println("Paid Rs. " + amountInRupees + " using Razorpay for invoice: " + invoiceId);
    }
}

// Adapter Class
// Allows RazorpayAPI to be used where PaymentGatewayGood is expected
class RazorpayAPIAdapter implements PaymentGatewayGood {
    private RazorpayAPIGood razorpayAPI;

    public RazorpayAPIAdapter() {
        this.razorpayAPI = new RazorpayAPIGood();
    }

    @Override
    public void pay(String orderId, double amount) {
        razorpayAPI.makePayment(orderId, amount);
    }
}

class CheckoutServiceGood {
    private PaymentGatewayGood paymentGateway;

    public CheckoutServiceGood(PaymentGatewayGood paymentGateway) {
        this.paymentGateway = paymentGateway;
    }

    public void checkout(String orderId, double amount) {
        paymentGateway.pay(orderId, amount);
    }
}

class MainGood {
    public static void main(String[] args) {
        CheckoutServiceGood checkoutService = new CheckoutServiceGood(new RazorpayAPIAdapter());
        checkoutService.checkout("12", 2000);
    }
}
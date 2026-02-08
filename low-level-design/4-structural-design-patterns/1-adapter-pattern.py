from abc import ABC, abstractmethod

# BAD EXAMPLE
# Target Interface: 
# Standard interface expected by the CheckoutService
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, order_id, amount):
        pass

# Concrete implementation of PaymentGateway for PayU
class PayUGateway(PaymentGateway):
    def pay(self, order_id, amount):
        print(f"Paid Rs. {amount} using PayU for order: {order_id}")

# Adaptee: 
# An existing class with an incompatible interface
class RazorpayAPI:
    def make_payment(self, invoice_id, amount_in_rupees):
        print(f"Paid Rs. {amount_in_rupees} using Razorpay for invoice: {invoice_id}")

# Client Class:
# Uses PaymentGateway interface to process payments
class CheckoutService:
    # Constructor injection for dependency inversion
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    # Business logic to perform checkout
    def checkout(self, order_id, amount):
        self.payment_gateway.pay(order_id, amount)

# Driver Code is at the bottom of the file

# GOOD EXAMPLE
# Target Interface: 
# Standard interface expected by the CheckoutService
class PaymentGatewayGood(ABC):
    @abstractmethod
    def pay(self, order_id, amount):
        pass

# Concrete implementation of PaymentGateway for PayU
class PayUGatewayGood(PaymentGatewayGood):
    def pay(self, order_id, amount):
        print(f"Paid Rs.{amount} using PayU for order: {order_id}")

# Adaptee: 
# An existing class with an incompatible interface
class RazorpayAPIGood:
    def make_payment(self, invoice_id, amount_in_rupees):
        print(f"Paid Rs.{amount_in_rupees} using Razorpay for invoice: {invoice_id}")

# Adapter Class:
# Allows RazorpayAPI to be used where PaymentGateway is expected
class RazorpayAdapterGood(PaymentGatewayGood):
    def __init__(self):
        self.razorpay_api = RazorpayAPIGood()
    
    # Translates the pay() call to RazorpayAPI's make_payment() method
    def pay(self, order_id, amount):
        self.razorpay_api.make_payment(order_id, amount)

# Client Class:
# Uses PaymentGateway interface to process payments
class CheckoutServiceGood:
    # Constructor injection for dependency inversion
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    # Business logic to perform checkout
    def checkout(self, order_id, amount):
        self.payment_gateway.pay(order_id, amount)

# Main method
if __name__ == "__main__":
    # BAD: Using PayU payment gateway to process payment (no adapter)
    checkout_service = CheckoutService(PayUGateway())
    checkout_service.checkout("12", 1780)

    print()

    # GOOD: Using razorpay payment gateway adapter to process payment
    checkout_service_good = CheckoutServiceGood(RazorpayAdapterGood())
    checkout_service_good.checkout("12", 1780)

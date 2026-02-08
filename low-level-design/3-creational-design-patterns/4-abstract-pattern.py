from abc import ABC, abstractmethod

# Bad Example
# Interface representing any payment gateway
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete implementation: Razorpay
class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing INR payment via Razorpay: {amount}")

# Concrete implementation: PayU
class PayUGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing INR payment via PayU: {amount}")

# Interface representing invoice generation
class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self):
        pass

# Concrete invoice implementation for India
class GSTInvoice(Invoice):
    def generate_invoice(self):
        print("Generating GST Invoice for India.")

# CheckoutService that directly handles object creation (bad practice)
class CheckoutService:
    def __init__(self, gateway_type):
        # Constructor accepts a string to determine which gateway to use
        self.gateway_type = gateway_type

    # Checkout process hardcodes logic for gateway and invoice creation
    def check_out(self, amount):
        # Hardcoded decision logic
        if self.gateway_type == "razorpay":
            payment_gateway = RazorpayGateway()
        else:
            payment_gateway = PayUGateway()

        # Process payment using selected gateway
        payment_gateway.process_payment(amount)

        # Always uses GSTInvoice, even though more types may exist later
        invoice = GSTInvoice()
        invoice.generate_invoice()

# Main method
if __name__ == "__main__":
    # Example: Using Razorpay
    razorpay_service = CheckoutService("razorpay")
    razorpay_service.check_out(1500.00)

# Good Example
# ========== Interfaces ==========
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self):
        pass

# ========== India Implementations ==========
class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing INR payment via Razorpay: {amount}")

class PayUGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing INR payment via PayU: {amount}")

class GSTInvoice(Invoice):
    def generate_invoice(self):
        print("Generating GST Invoice for India.")

# ========== US Implementations ==========
class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing USD payment via PayPal: {amount}")

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing USD payment via Stripe: {amount}")

class USInvoice(Invoice):
    def generate_invoice(self):
        print("Generating Invoice as per US norms.")

# ========== Abstract Factory ==========
class RegionFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self, gateway_type):
        pass

    @abstractmethod
    def create_invoice(self):
        pass

# ========== Concrete Factories ==========
class IndiaFactory(RegionFactory):
    def create_payment_gateway(self, gateway_type):
        if gateway_type == "razorpay":
            return RazorpayGateway()
        elif gateway_type == "payu":
            return PayUGateway()
        raise ValueError(f"Unsupported gateway for India: {gateway_type}")

    def create_invoice(self):
        return GSTInvoice()

class USFactory(RegionFactory):
    def create_payment_gateway(self, gateway_type):
        if gateway_type == "paypal":
            return PayPalGateway()
        elif gateway_type == "stripe":
            return StripeGateway()
        raise ValueError(f"Unsupported gateway for US: {gateway_type}")

    def create_invoice(self):
        return USInvoice()

# ========== Checkout Service ==========
class CheckoutService:
    def __init__(self, factory, gateway_type):
        self.payment_gateway = factory.create_payment_gateway(gateway_type)
        self.invoice = factory.create_invoice()

    def complete_order(self, amount):
        self.payment_gateway.process_payment(amount)
        self.invoice.generate_invoice()

# ========== Main Method ==========
if __name__ == "__main__":
    # Using Razorpay in India
    india_checkout = CheckoutService(IndiaFactory(), "razorpay")
    india_checkout.complete_order(1999.0)

    print("---")

    # Using PayPal in US
    us_checkout = CheckoutService(USFactory(), "paypal")
    us_checkout.complete_order(49.99)

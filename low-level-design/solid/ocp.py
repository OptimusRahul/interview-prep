from abc import ABC, abstractmethod
# Open/Closed Principle

# Voilation of Open/Closed Principle
class InvoiceCalculatorVoilation:
    def calculateTotal(self, region, amount):
        if region == "IN":
            return amount * 1.05
        elif region == "US":
            return amount * 1.05
        elif region == "EU":
            return amount * 1.05
        else:
            return amount


class InvoiceCalculator(ABC):
    @abstractmethod
    def calculateTotal(self, amount):
        pass

class INInvoiceCalculator(InvoiceCalculator):
    def calculateTotal(self, amount):
        return amount * 1.05

class USInvoiceCalculator(InvoiceCalculator):
    def calculateTotal(self, amount):
        return amount * 1.05

class EUInvoiceCalculator(InvoiceCalculator):
    def calculateTotal(self, amount):
        return amount * 1.05

class Invoice:
    def __init__(self, amount, taxCalculator):
        self.amount = amount
        self.taxCalculator = taxCalculator

    def getTotalAmount(self):
        return self.amount + self.taxCalculator.calculateTotal(self.amount)

amount = 1000.0

indiaInvoice = Invoice(amount, INInvoiceCalculator())
usInvoice = Invoice(amount, USInvoiceCalculator())
euInvoice = Invoice(amount, EUInvoiceCalculator())

print(indiaInvoice.getTotalAmount())
print(usInvoice.getTotalAmount())
print(euInvoice.getTotalAmount())
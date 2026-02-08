"""
You are required to design an interface PaymentGateway that defines a common method for processing payments. Implement two classes, CreditCardPayment and UPIPayment, which provide specific implementations of the processPayment() method. Use polymorphism to demonstrate how different payment methods can be processed through the same interface.

Interface PaymentGateway :

Abstract Method processPayment( double amount ) : This method processes a payment of the specifies amount.
Implementing classes :

CreditCardPayment :

Method :

processPayment( double amount ) : Implements to print "Processing credit card payment of amount".
UPIPayment

Method :

processPayment( double amount ) : Implements to print "Processing UPI payment of amount".


Refer the sample input example to understand about the output format.

Refer the commented code on IDE for output statements.
"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def processPayment(self, amount: float):
        pass

class CreditCardPayment(PaymentGateway):
    def processPayment(self, amount: float):
        print(f"Processing credit card payment of {amount:.2f}")

class UPIPayment(PaymentGateway):
    def processPayment(self, amount: float):
        print(f"Processing UPI payment of {amount:.2f}")

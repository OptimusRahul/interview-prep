from typing import List
class BankAccount:
    # Constructor
    def __init__(self, accountHolderName, balance):
        self.__accountHolderName = accountHolderName  # Private attributes
        self.__balance = balance

    # Public getter for accountHolderName
    def getAccountHolderName(self):
        return self.__accountHolderName

    # Public setter for accountHolderName
    def setAccountHolderName(self, accountHolderName):
        self.__accountHolderName = accountHolderName

    # Public getter for balance
    def getBalance(self):
        return self.__balance

    # Public setter for balance (only allows positive deposits)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

# Main
if __name__ == "__main__":
    # Creating an object of BankAccount
    account = BankAccount("John Doe", 5000)

    # Using getter to access private data
    print("Account Holder:", account.getAccountHolderName())
    print("Balance:", account.getBalance())

    # Modifying balance using setter method
    account.deposit(1500)
    print("Updated Balance:", account.getBalance())

    # Trying to withdraw an amount
    account.withdraw(2000)
    print("Balance after Withdrawal:", account.getBalance())



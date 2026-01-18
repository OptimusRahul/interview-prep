class BankAccount:
    accountNumber: str
    balance: float

    def __init__(self, accountNumber: str, balance: float):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")
            self.displayDetails()
    
    def displayDetails(self):
        print("Account Number : " + self.accountNumber)
        print("Balance : {:.2f}".format(self.balance))

if __name__ == "__main__":
    # Hardcoded input
    accountNumber = "9662375274869"
    balance = 8655
    addBalance = 5854
    withdrawBalance = 9437

    # Create BankAccount object
    account = BankAccount(accountNumber, balance)

    # Deposit and withdraw operations
    account.deposit(addBalance)
    account.withdraw(withdrawBalance)

    # Display final account details
    account.displayDetails()

from datetime import datetime, timedelta

class Bankaccount:
    def __init__(self, account_number, account_holder, balance=0.00):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit value should be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw a positive amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account holder: {self.account_holder}, Account number: {self.account_number}, Account balance: {self.balance:.2f}"

class Savingsaccount(Bankaccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.00):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

class Currentaccount(Bankaccount):
    def __init__(self, account_number, account_holder, overdraft_limit, balance=0.00):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw a positive amount")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Exceeded overdraft limit")
        self.balance -= amount

class Fixed_deposit(Bankaccount):
    def __init__(self, account_number, account_holder, lockin_time, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.lockin_time = lockin_time
        self.creation_time = datetime.now()

    def withdraw(self, amount):
        if datetime.now() < self.creation_time + timedelta(days=self.lockin_time):
            raise ValueError("Cannot withdraw before lock-in period")
        super().withdraw(amount)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer_Account(self, from_account_no, to_account_no, amount):
        from_account = self.get_account(from_account_no)
        to_account = self.get_account(to_account_no)

        if from_account is None or to_account is None:
            raise ValueError("Need two valid account details")
        from_account.withdraw(amount)
        to_account.deposit(amount)

# Create bank instance
bank = Bank()

# Create accounts
savings = Savingsaccount("787878", "Chris", interest_rate=5, balance=1000)
current = Currentaccount(account_number="454545", account_holder="Ben", overdraft_limit=1000, balance=750)
fixed = Fixed_deposit(account_number="666666", account_holder="Bob", lockin_time=0, balance=1000)  

# Add accounts to bank
bank.add_account(savings)
bank.add_account(fixed)
bank.add_account(current)

# Perform transfer
bank.transfer_Account("666666", "454545", 200)

# Print account details
print(bank.get_account("666666"))
print(bank.get_account("454545"))

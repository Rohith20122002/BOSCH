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
        print("After deposit balance:",amount)
        print("\n")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw a positive amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print("After withdraw balance:",amount)

    def get_balance(self):
        b=self.balance
        print("BANK BALANCE:",b)
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
        self.creation_time = datetime(2024, 9, 1, 14, 30, 45)
        print("\n")
        print("Time when deposited is :",self.creation_time)
        

    def withdraw(self, amount):
        if datetime.now() < self.creation_time + timedelta(days=self.lockin_time):
            raise ValueError("Cannot withdraw before lock-in period")
        lt=self.creation_time + timedelta(days=self.lockin_time)
        print("The time you can withdraw is:",lt)
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


bank = Bank()


savings = Savingsaccount("12343", account_holder="rohith", interest_rate=9, balance=1000)
current = Currentaccount(account_number="76790", account_holder="sujan", overdraft_limit=2000, balance=900)
fixed = Fixed_deposit(account_number="666666", account_holder="karthik", lockin_time=2, balance=300)  


bank.add_account(savings)
bank.add_account(fixed)
bank.add_account(current)
print("BEFORE TRANSFER \n")
print(bank.get_account("666666"))
print(bank.get_account("12343"))

bank.transfer_Account("666666", "12343", 200)


print("AFTER TRANSFER\n")
print(bank.get_account("666666"))
print(bank.get_account("12343"))

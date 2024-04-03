class BankAccount:
    def __init__(self, account_number, account_name, account_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_balance = account_balance

    def get_balance(self):
        return self.account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
            return
        self.account_balance -= amount
        return self.account_balance

class ATM:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_balance(self, account_number):
        account = self.find_account(account_number)
        if account is not None:
            print(f"The balance of account number {account_number} is ${account.get_balance():.2f}")
        else:
            print("No account with this number was found")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account is not None:
            account.deposit(amount)
            print(f"${amount:.2f} has been deposited. Your new balance is ${account.get_balance():.2f}")
        else:
            print("No account with this number was found")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account is not None:
            account.withdraw(amount)
            print(f"${amount:.2f} has been withdrawn. Your new balance is ${account.get_balance():.2f}")
        else:
            print("No account with this number was found")

class BankAccount():
    
    def __init__(self, int_rate = .01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Decline')
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f'New balance is {self.balance}') 
            return self
        else:
            return None

account1 = BankAccount(int_rate= .05, balance= 500)
account2 = BankAccount()
account1.display_account_info().deposit(2000).deposit(300).deposit(500).withdraw(1300).display_account_info().yield_interest()
account2.display_account_info().deposit(300).deposit(900).withdraw(17).withdraw(3000).withdraw(567).withdraw(69).display_account_info().yield_interest()
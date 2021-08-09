class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.irate = int_rate
        self.bal = balance
        
    def deposit(self, amount):
        self.bal += amount
        return self
    
    def withdraw(self, amount):
        if self.bal < amount:
            self.bal -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.bal -= amount
        return self
    
    def display_account_info(self):
        print(f'Account Balance: ${self.bal}\nInterest rate:{self.irate}\n')
        return self
    
    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal * self.irate
        return self

Bob = BankAccount(0.01,500)
Kim = BankAccount(0.01,1000)

#1 first user - 3 deposits / 1 withdrawal / Add Yielded_interest / Display Info
Bob.deposit(50).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()

#2 Second user - 1 deposit / 4 withdrawals / Add Yielded_interest / Display Info
Kim.deposit(50).deposit(50).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

#3 Second user - 1 withdrawal insufficient funds / Display Info
Bob.withdraw(1000).display_account_info()
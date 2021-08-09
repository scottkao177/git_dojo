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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(int_rate=0.0, balance=0)	# link checking account with BankAccount methods
        self.savings = BankAccount(int_rate=0.02, balance=500)  # Add saving account type
        self.cd = BankAccount(int_rate=0.1, balance=1000)       # Add certificate of deposit account type
#create BankAccount methods here
    #deposit
    #checking
    def deposit_checking(self,amount): # method called upon by user to deposit
        self.checking.deposit(amount)  # self(user) > checking(linking checking account type from User attributes) > deposit(linking deposit method from Bank Account class)
        return self                    # return to user and sets up chaining
    #savings
    def deposit_savings(self,amount): 
        self.savings.deposit(amount)
        return self
    #certificate of deposit
    def deposit_cd(self,amount):
        self.cd.deposit(amount)
        return self

    #withdraw
    #checking
    def withdraw_checking(self,amount):
        self.checking.withdraw(amount)
        return self
    #savings
    def withdraw_savings(self,amount):
        self.savings.withdraw(amount)
        return self
    #certificate of deposit
    def withdraw_cd(self,amount):
        self.cd.withdraw(amount)
        return self

    #Display_balance
    #checking
    def display_checking(self):
        print("Checking")
        self.checking.display_account_info()
        return self
    #savings
    def display_savings(self):
        print("Savings")
        self.savings.display_account_info()
        return self
    #cd
    def display_cd(self):
        print("Certificate of Deposit")
        self.cd.display_account_info()
        return self

bob = User('bob','bob@gmail.com')

bob.deposit_checking(1000).withdraw_checking(500).display_checking().deposit_savings(100).withdraw_savings(300).display_savings()
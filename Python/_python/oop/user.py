class User:
    def __init__(self, username, email_address):
        #attributes
        self.name = username
        self.email = email_address
        self.account_bal = 0
        
    #methods
        #deposit
    def make_deposit(self, amount):
        self.account_bal += amount
        return self
        #withdrawal
    def make_withdrawal(self, amount):
        self.account_bal -= amount
        return self
    def transfer_money(self, other_user, amount):
        self.account_bal -= amount
        other_user.account_bal += amount
        return self
    def display_user_balance(self):
        print(f"{self.name} - account balance: {self.account_bal}")
        return self

#instances & adding values to them
astra = User('Astra Militarum', 'Guard@Imperium.man')
astartes = User('Adeptus Astartes', 'Astartes@Imperium.man')
inquisition = User('Ordos Hereticus', 'Hereticus@Imperium.man')

#calling methods
#first user
astra.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance() 
#output - account balance: 200

#second user
astartes.make_deposit(500).make_deposit(100).make_withdrawal(100).make_withdrawal(100).display_user_balance() 
#output - account balance: 400

#third user
inquisition.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance() 
#output - account balance: 700

#first user transfer to third user (BONUS)
astra.transfer_money(inquisition, 200).display_user_balance() 
#output - account balance: 0
inquisition.display_user_balance() 
#output - account balance: 900



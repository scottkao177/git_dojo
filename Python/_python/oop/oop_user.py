class User:
    def __init__(self, username, email_address):
        #attributes
        self.name = username
        self.email = email_address
        self.account_bal = 0
        
    #methods
    def make_deposit(self, amount):
        self.account_bal += amount

#instances & adding values to them
adeptus = User('Adeptus Astartes', 'Astartes@Imperium.net')
poto = User('Potosan', 'potosan@hotmail.com')

#calling methods
adeptus.make_deposit(100)
print(adeptus.account_bal) #output 100
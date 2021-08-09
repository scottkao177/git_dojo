# OOP (Object Oriented Programming)
# Faster, Efficient, Repeatable

#C-cup example
#Think about different cups and their physical appearance
    #1 what is the material of the cup?
    #2 what color is it?
    #3 How tall is it?

class Cup:
    def _init_(self, materialOfCup, colorOfCup):
        # What does the cup have? (attributes)
        self.material
        self.color
        self.percent_filled
        
        # What can the cup do? (methods)
    def fill(self,amountofLiquid):
        self.percent_filled += amountofLiquid
        
    def pour(self,amountofLiquid):
        self.percent_filled -= amountofLiquid
    
    def spill(self):
        self.percent_filled = self.percent_filled / 2
    
    def say_info(self):
        print(f"This {self.material}, {self.color} cup is {self.percent_filled}% full.")

#Different types of cups (Instances)
# paperCup = Cup("paper","white")
myFavoriteCup = Cup()
plasticCup = Cup()

#Calling methods (Initiating the actions from methods)
myFavoriteCup.fill(60)
myFavoriteCup.pour()
myFavoriteCup.spill(10)
myFavoriteCup.say_info()







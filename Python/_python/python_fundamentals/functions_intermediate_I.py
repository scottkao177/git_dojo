# print(randInt()) 		    # should print a random integer between 0 to 100
import random
def randInt():
    num = random.random()*100
    return round(num)
print(randInt())

# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
import random
def randInt(max=50):
    num = random.random()*max
    return round(num)
print(randInt(max=50))

# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
import random
def randInt(min=50):
    num = random.random()*min+50
    return round(num)
print(randInt(min=50))

# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
import random
def randInt(min=50, max=500):
    num = random.random()*min+(max-50)
    return round(num)
print(randInt(min=50, max=500))




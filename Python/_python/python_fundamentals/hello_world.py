#1
print ("Hello World")

#2
name = "Scott"
print ("Hello", name)
print ("Hello " + name)

#3
name = 40000
print ("Hello", name)
# print ("Hello " + name)

#4a
fave_food1 = "Roast Beef"
fave_food2 = "Baked Potato"
print(f"My two real favorite foods are {fave_food1} and {fave_food2}!")

#4b
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "My two favorite foods are {} and {}!" .format(fave_food1, fave_food2))

#Ninja Bonus
name = "Adeptus Astartes"
chant = "For the Emperor!"
time = 40
print ("The %s in %dK are known to yell %s when going into battle." %(name, time, chant))

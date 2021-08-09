#1
for x in range (151):
    print(x)

#2
for x in range (5, 1005, 5):
    print(x)

#3
for x in range (1,101):
    if (x % 5 == 0):
        print("Coding")
    elif (x % 10 == 0):
        print("Coding Dojo")
    else:
        print(x)

#4
sum = 0
for x in range (0, 500000):
    if (x % 2 != 0):
        sum += x
print(sum)

#5
for x in range (2018, 0, -4):
    print(x)

#6
lowNum = 2
highNum = 9
mult = 3
for x in range (lowNum, highNum+1, 1):
    if (x % mult == 0):
        print(x)




#1
#Change all positives numbers in the list to "big"
def big(biggie_size):
    list = []
    for index in range(len(biggie_size)):
        if biggie_size[index] > 0:
            list.append('big')
        else:
            list.append(biggie_size[index])
    return list
# Stating Variable biggie_size + calling function big(biggie_size)
biggie_size = [-1, 3, 5, -5]
print('#1',big(biggie_size))

#2
# Count positives & return with replacing last element with amount
def rep(x):
    list = []
    count = 0
    for i in range(len(x)):
        if x[i] > 0:
            count += 1
            list.append(x[i])
        elif x[i] < 0:
            list.append(x[i])
    #remove last element
    list.pop(-1)
    #add count(4) to end of list
    list.append(count)
    return list
# Stating Variable x + function rep(x)
x = -3,-2,1,3,5,10
print('#2 List + replace last element with positive count:', rep(x))

#3
# Total Sum
def sum(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total
# Stating variable x + calling function sum(x)
x = 1,2,3,4,5
print('#3 Total sum of x:',sum(x))

#4
# return average of all values
def avg(x):
    list = []
    for i in range(len(x)):
        list.append(x[i])
    return list
#activate statistics method to calculate average
import statistics
x = 3,3,5
print ('#4 Average of x:', statistics.mean(avg(x)))

#5
# Return the length of list
def length(x):
    count = 0
    for i in range(len(x)):
        count += 1
    return count
#Stating variable x + calling function length(x)
x = 1,2,3,4,5,6,7,8,10,15
print('#5 length of x is:',length(x))

#6
# return minimum value
def minimum(x):
    min = []
    for i in range(len(x)):
        min.append(x[i])
    return min

x = 3,4,5,-7
print('#6 min value:', min(minimum(x)))

#7
# return max value
def maximum(x):
    max = []
    for i in range(len(x)):
        max.append(x[i])
    return max

x = 3,4,5,-7
print('#7 max value:', max(maximum(x)))

#8
# return sumTotal, average, minimum, maxmimum, and length of list.
def ultimate(x):
    list = []
    for i in range(len(x)):
        list.append(x[i])
    return list

x = 3,4,5,-7
print('#8 Ultimate Analysis -','sum:',sum(ultimate(x)),'avg:', statistics.mean(ultimate(x)),'min:',min(ultimate(x)),'max:',max(ultimate(x)),'length:',len(ultimate(x)))

#9
#reverse the list
def reversal(x):
    #return reversed list of x
    return [i for i in reversed(x)]

x = 1,3,5,9,11
print('#9 Reversed List:', (reversal(x)))

sum()
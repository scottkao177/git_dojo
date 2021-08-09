#1
def countdown():
    for x in range (n, 0-1, -1):
        print (x)

n = (int(5))
countdown()

#2
def pR(a,b):
    print("Print", a)
    a = b
    return print("Return", a)

pR(1,2)

#3
def first_add_length(x):
    return print(x[0] + len(x))

x = 1,2,3,4,5
first_add_length(x)

#4
def Values_Greater_2nd(list):
    small_list = []
    great_list = []
    second_value = list[1]
    for i in range(len(list)):
        if list[i] < second_value:
            small_list.append(list[i])
        elif list[i] > second_value:
            great_list.append(list[i])

    print(len(great_list), len(small_list))
    return (great_list, small_list)

list = 6,3,4,5,0,1
print(Values_Greater_2nd(list))

#5
def l_and_v(size, value):
    list = []
    for x in range(size):
        list.append(value)
    return list

print(l_and_v(4,2))








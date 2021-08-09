#part 1
x = [ [5,2,3],[10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1a Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def change_val(x):
    x[1][0] = 15
    return x
print(change_val(x))

#1b Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_lname(students):
    students[0]["last_name"]="Bryant"
    return students
print(change_lname(students))

#1c In the sports_directory, change 'Messi' to 'Andres'
def sports(sports_directory):
    sports_directory["soccer"][0]="Andres"
    return sports_directory
print(sports(sports_directory))

#1d Change the value 20 in z to 30
def value(z):
    z[0]["y"]=30
    return z
print(value(z))

#part 2
students_2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary(students_2):
    w =  "first_name - " + students_2[0]["first_name"], "last_name - " + students_2[0]["last_name"]
    x =  "first_name - " + students_2[1]["first_name"], "last_name - " + students_2[1]["last_name"]
    y =  "first_name - " + students_2[2]["first_name"], "last_name - " + students_2[2]["last_name"]
    z =  "first_name - " + students_2[3]["first_name"], "last_name - " + students_2[3]["last_name"]
    return w,x,y,z
print(iterateDictionary(students_2))
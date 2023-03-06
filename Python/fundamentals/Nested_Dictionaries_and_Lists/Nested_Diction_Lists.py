# 1) Update Values in Dictionaries and Lists
# 

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print("----------------Start Number 1----------------")
print("This is the start of the x list")
print("======================")
print(type(x))
print(x)
x[1][0] = 15
print(x)
print(f"\n")


print("----------------Start Number 2----------------")
print("This is the start of the student list")
print("======================")
print(type(students))
print(students)
print(students[0]["first_name"])
students[0]["last_name"] = "Bryant"
print(students)
print(f"\n")

print("----------------Start Number 3----------------")
print("This is the start of the sports_directory dictionary")
print("======================")
print(type(sports_directory))
print(sports_directory)
print(sports_directory["soccer"][0])
sports_directory["soccer"][0] = "Andres"
print(sports_directory)


print("----------------Start Number 4----------------")
print("This is the start of the z list")
print("======================")
print(type(z))
print(z[0]["y"])
z[0]["y"] = 30
print(z)
print(f"\n")

#
#

# 2) Iterate Through a List of Dictionaries
print("----------------Start Iterate List of Dictionaries----------------")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary():
        for name in students:
            print('first_name - {}, last_name - {} '.format('name[0]' , 'name[1]')) # with .format()
            #print(f"first_name - " + {name["first_name"]} + "," + "last_name - " + {name["last_name"]})
iterateDictionary()

print(f"\n")
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



# Get Values From a List of Dictionaries
print("----------------Get Values From List of Dictionaries (First Name)----------------")

students_2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2():
    for x in range(len(students_2)):
        print(students_2[x]["first_name"])
iterateDictionary2()
print(f"\n")

print("----------------Get Values From List of Dictionaries (Last Name)----------------")
def iterateDictionary3():
    for x in range(len(students_2)):
        print(students_2[x]["last_name"])
iterateDictionary3()
print(f"\n")


# Iterate Through a Dictionary with List Values
print("----------------Iterate Through Dictionary with List of Values (Locations)----------------")


# dojo list 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

number_of_locations = len(dojo["locations"])
print(f" {number_of_locations} LOCATIONS")


def printinfo():
    for x in range(len(dojo["locations"])):
        print(dojo["locations"])
printinfo()
print(f"\n")


number_of_instructors = len(dojo["instructors"])
print(f" {number_of_instructors} INSTRUCTORS")

def printinfo2():
    for x in range(len(dojo["instructors"])):
        print(dojo["instructors"])
printinfo2()
print(f"\n")
num1 = 42  # variable declaration
num2 = 2.3  # variable declaration
boolean = True   # variable declaration  and Boolean
string = 'Hello World'  # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']     # List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # Dictionary 
fruit = ('blueberry', 'strawberry', 'banana')  # Tuple
print(type(fruit))    # type check
print(pizza_toppings[1])  # List  - Access Value 
pizza_toppings.append('Mushrooms')   # List  - Add Value 
print(person['name'])   # Dictionary - Access Value 
person['name'] = 'George'   # Dictionary - Change Value
person['eye_color'] = 'blue'  # Dictionary  - IndexError: list index out of range
print(fruit[2])   # Tuple -- - access value

if num1 > 45:   # Conditional -  if : else 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:  # Conditional  - if : elif : else 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):   # For Loop
    print(x)
for x in range(2,5):  # For Loop
    print(x)
for x in range(2,10,3):    # For Loop
    print(x)
x = 0        # variable declaration
while(x < 5):   # While Loop
    print(x)
    x += 1

pizza_toppings.pop()   # AttributeError: 'tuple' object has no attribute 'pop'
pizza_toppings.pop(1)  # AttributeError: 'tuple' object has no attribute 'pop'

print(person)    # Dictionary Access Value
person.pop('eye_color')   #  IndexError: list index out of range
print(person)   # Dictionary Access Value

for topping in pizza_toppings:   # For Loop
    if topping == 'Pepperoni':   # Conditional
        continue
    print('After 1st if statement')   
    if topping == 'Olives':   # Conditional
        break

def print_hello_ten_times():  # Function 
    for num in range(10):
        print('Hello')

print_hello_ten_times()    #  NameError: name <variable name> is not defined

def print_hello_x_times(x):   #   Function 
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #  NameError: name <variable name> is not defined

def print_hello_x_or_ten_times(x = 10): # Function
    for num in range(x):   # For Loop
        print('Hello')

print_hello_x_or_ten_times()   #  NameError: name <variable name> is not defined
print_hello_x_or_ten_times(4)   


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'   #  IndexError: list index out of range
# print(person['favorite_team'])   # Dictionary  - IndexError: list index out of range
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
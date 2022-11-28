num1 = 42  #variable declaration. integer
num2 = 2.3  #variable declaration. float
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #list access
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #print value from dictionary
person['name'] = 'George' #change value of name key
person['eye_color'] = 'blue' #change value of eye color key
print(fruit[2]) #print banana

if num1 > 45:   #conditional if
    print("It's greater") 
else: #conditional else
    print("It's lower")

if len(string) < 5: #conditional if
    print("It's a short word!")
elif len(string) > 15: #else if  statement
    print("It's a long word!")
else: #conditional else statement
    print("Just right!")

for x in range(5): #for loop with defined times of loop, start
    print(x)
for x in range(2,5): #for loop with range of loops with starting with 2, start
    print(x)
for x in range(2,10,3): 
    print(x)
x = 0
while(x < 5): #while loop with conditional to stop
    print(x)
    x += 1 #increment

pizza_toppings.pop() #delete last value from list
pizza_toppings.pop(1) #delete 2nd value from list

print(person) #log statement
person.pop('eye_color') #remove eye color from dictionary
print(person) #print person dictionary with eye color key removed

for topping in pizza_toppings:    #loop through pizza_toppings list
    if topping == 'Pepperoni': #conditional if statement
        continue  #continue with loop even after conditional is met
    print('After 1st if statement') #sequence
    if topping == 'Olives': #if conditional
        break #break statement to end loop

def print_hello_ten_times(): #function delcaration
    for num in range(10): #loop start 10 times
        print('Hello') # print hello to log statement

print_hello_ten_times() #function invocation

def print_hello_x_times(x): #function declaration with X as a parameter
    for num in range(x): #for loop start passing in x argument in range
        print('Hello') 

print_hello_x_times(4) #function invocation

def print_hello_x_or_ten_times(x = 10): #function declaration
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() #function invocation that will print 10 times
print_hello_x_or_ten_times(4) #function invocation that will print 4 times


"""
Bonus section
"""

print(num3) #name error
num3 = 72 # variable declaration
fruit[0] = 'cranberry' #cannot change value on tuple
print(person['favorite_team']) #keyError, key is not defined
print(pizza_toppings[7]) #index error
  print(boolean) #index error
fruit.append('raspberry') #attributeError cannot append to a tuple
fruit.pop(1) #attributeError cannot pop a tuple
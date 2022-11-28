# print("Hello World!")

# x = "Hello Python"
# print(x)
# y = 42
# print(y)


# x = 10
# if x > 50:
#     print("bigger than  50")
# else:
#     print("smaller than 50")

# class EmptyClass:
#     pass
# is_hungry = True
# has_freckles = False

# age = 35
# weight = 160.57

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# empty_dict = {}
# new_person = {'name': 'John', 'age':38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)
# w = new_person.pop('weight')
# print(w)
# print(new_person)
# print(type(2.63))
# print(type(new_person))

# print(len(new_person))
# print(len('Coding Dojo'))

# float_to_int = int(3.7)
# int_to_float = float(56)
# int_to_complex = complex(33)

# print(float_to_int)
# print(int_to_float)
# print(int_to_complex)

# import random
# print(random.randint(1,20))

# first_name = 'Zen'
# last_name = 'Coder'
# age = 27
# print("My first name is {} {} and I am {} years old.".format(first_name, last_name, age))
def print_hello_x_or_ten_times(x = 10): #function declaration
    for num in range(x): #for loop start
        print('Hello') #log statement
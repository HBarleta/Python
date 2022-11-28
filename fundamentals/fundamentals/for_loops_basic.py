#basic
for i in range(151):
    print(i)

#Multiples of Five
for i in range(5, 1000):
    if(i % 5 == 0):
        print(i)

#counting, the dojo way
for i in range(1, 100):
    if (i % 10 == 0):
        print("Coding")
    elif (i % 5 == 0):
        print("Coding Dojo")
#whoa, that suckers huge
output = 0
for i in range(500001):
    output += i

print(output)

#countdown by fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if(i % 3 == 0):
        print(i)
print("Exercises: Level 1")

numbers = [0,1,2,3,4,5,6,7,8,9,10] #For,
for number in numbers: 
    print(number)

count = 0 
while count <10: 
    print(count)
    count = count +1

numbers = [10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)

count = 10
while count <0:
    print(count)
    count = count - 1

calls = "#"
while calls < "########":
    print(calls)
    calls= calls + "#"

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
    
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]
for num1,num2 in zip(num1,num2):
    print(f"{num1} x {num2} =", num1*num2)

lenguajes_programacion  =['Python', 'Numpy','Pandas','Django', 'Flask']
for lenguajes in lenguajes_programacion :
    print( lenguajes)

for num in range(0, 101):
    if num % 2 == 0:
        print(num)

for num in range(0, 101):
    if num % 2 != 0:
        print(num)














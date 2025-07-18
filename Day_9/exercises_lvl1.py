print("Exercises: Level 1")

age = int(input("Escribe tu edad:"))
if age >= 18:
    print("You are old enough to learn drive.")
else :
    print(f"you need  {18 - age} more years to learn to drive. ")

my_age = int(input("Escribe tu edad:"))
your_age = int(input("Escribe tu edad:"))
print("Quien es mas grande tu o yo: ")
if my_age == your_age :
    print("Tenemos la misma edad.")
elif my_age < your_age :
    print(f"Tu eres { your_age - my_age} años mayor que yo.")
else :
    print(f"Yo soy {my_age - your_age} años mayor que tu. ")

numero_a =int(input("Escribe el primer numero :")) 
numero_b = int(input("Escribe el segundo numero:"))
if numero_a == numero_b :
    print("Los numeros son iguales.")
elif numero_a < numero_b :
    print(f"El numero {numero_a} es menor que el {numero_b}.")
else : 
    print(f"El numero {numero_a} es mayor que el {numero_b}.")
































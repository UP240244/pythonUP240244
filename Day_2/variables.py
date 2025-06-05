#Day 2: 30 Days of python programming

#Exercise: level 1
#declaración de variables 

first_name="Alison"
last_name="Romo"
full_name="Alison Romo"
country="Mexico"
city="Aguascalientes" 
age=19
year=2025
is_married=False
is_true=True
is_light_on=False
num1, num2, num3= 10, 15, 20

#exercise: level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(num1))
print(type(num2))
print(type(num3))

print(len(first_name))
print("Longitud nombre:", len(first_name), " Longitud apellido:", len(last_name))
num_one=5
num_two=4
total=num_one+num_two
print(total)
diff=num_one-num_two
print(diff)
product=num_one*num_two
print(product)
division=num_one/num_two
print(division)
remainder=num_two%num_one
print(remainder)
exp=num_one**num_two
print(exp)
floor_division=num_one//num_two
print(floor_division)

print("Circulo de 30 metros de radio")

area_of_circle=30*(3.14**2)
circum_of_circle=3.14*(30*2)
print("El area del circulo es:", area_of_circle)
print("La circunferencia del circulo es:", circum_of_circle)
print("Nuevo circulo")
radio= input("Ingresa el radio del circulo: ")
area=int(radio)*(3.14**2)
print("El area del circulo es: ", area)
nombre, apellido, pais, edad= input("Ingrese su nombre, apellido, país y edad: ").split()
print(nombre, apellido, pais, edad)

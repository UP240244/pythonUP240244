age=18
height=1.59
n_com=2+3j

print("Área del triangulo")

base=float(input("Ingresa la base del triángulo: "))
altura=float(input("Ingresa la altura del triángulo: "))
print("El área total del triangulo es de:",(base*altura)/2)

print("Perimetro del triángulo")

lado_a=float(input("Introduce el lado a del triángulo: "))
lado_b=float(input("Introduce el lado b del triángulo: "))
lado_c=float(input("Introduce el lado c del tríangulo: "))

print("El perimetro del triángulo es de: ", lado_a+lado_b+lado_c)

print("Área y perimetro de un rectángulo")

ancho= float(input("Introduce el ancho del rectángulo: "))
largo = float(input("Introduce el largo del rectángulo: "))

print("El área del rectángulo es de: ", largo*ancho)
print("El perimetro del rectángulo es de: ", 2*(largo*ancho))

print("Área y circunferencia de un circulo")

radio=float(input("Introduce el radio del circulo: "))
print("El área del circulo es de: ", 3.14*(radio**2))
print("La circunferencia del circulo es de: ", 2*3.14*radio)

print("Pendiente dada la formula y=2x-2")

x1,y1= 0,-2
x2,y2=1,0
print("La pendiente es de: ",(y2-y1)/(x2-x1))

print("Pendiente con los puntos (2,2) y (6,10)")

x1,y1= 2,2
x2,y2=6,10
print("La pendiente es de: ", (y2-y1)/(x2-x1))

print("Valores de x")

for x in range (-7,7):
    y=x**2+6*(x)+9
    print("El valor de y es de: ", y)
    if (y==0):
        print("El valor de y es 0 cuando x tiene el valor de: ", x)

print("Lonitud y comparación de las palabras python y dragon")

p1="Python"
p2="Dragon"
lon1=len(p1)
lon2=len(p2)
falsy_comparation=lon1>lon2
print("El número de letras de ",p1," es de: ",lon1)
print("El número de letras de ", p2," es de: ",lon2)
print("El resultado de la comparación es: ", falsy_comparation)

print("Verificar la terminación de ambas palabras")

con_on=('on' in p1) and ('on' in p2)
print("¿Se encuentra la terminación on en ambas palabras? ", con_on)

print("¿Se encuentra la palabra?")

frase="I hope this course is not full of jargon"
con_jargo=('jargon' in frase)
print("¿Se encuentra la palabra jargon? ", con_jargo)

print("Longitud y conversión de flotante y string")

lon1_float=float(lon1)
lon1_str=str(lon1_float)
print(type(lon1_float))
print(type(lon1_str))

print("Número par o impar")

num=int(input("Ingrese el número: "))
if (num%2==0):
    print("El número es par")
else:
    print("El número es impar")

print("Floor division")

residuo=7//3
v_entero=int(2.7)
comp=residuo==v_entero
print("¿La comparación es verdadera? ", comp)

print("Igualdad")

v_int=10
v_str="10"
comp2=v_int==v_str
print("¿Las variables son iguales? ", comp2)

print("Comparación entre 9.8 y 10")

v1=int(9.8)
v2=10
comp3=v1==v2
print("¿Son iguales? ", comp3)

print("Horas y tarifa")

horas=int(input("Ingrese las horas: "))
tarifa=float(input("Ingrese la tarifa: "))
pago=horas*tarifa
print("El total a pagar es de: ", pago)

print("Edad a segundos")

años=int(input("Ingrese la cantidad de años que usted ha vivido: "))
print("Usted ha vivido durante ", (31557600*años), " segundos")

print("Tabla")

for i in range  (1,6):
    print(f"{i} 1 {i} {i**2} {i**3}")

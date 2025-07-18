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

print("Exercises: Level 2")

scores = int(input("Ingresa la calificacion:")) 
if scores>= 80:
    print('Tu calificacion es: A')
elif scores > 70 and scores < 79:
    print('Tu calificacion es: B')
elif scores > 60 and scores < 69:
    print('Tu calificacion es: C')
elif scores > 50 and scores < 59:
    print('Tu calificacion es: D')
else:
    print('Tu calificacion es: F')

mes = input('Ingresa el mes:').capitalize()
if mes in ['Septiembre','Octubre','Noviembre']:
    print('La estacion es otoño')
elif mes in ['Diciembre','Enero','Febrero']:
    print('La estacion es invierno')
elif mes in ['Marzo','Abril','Mayo']:
    print('La estacion es primavera')

frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_si_son_existentes = input("Escriba la fruta que quiera:").lower()
if frutas_si_son_existentes in frutas :
    print("La fruta que buscas si existe en la lista")
else : 
    frutas.append(frutas_si_son_existentes)
    print("La fruta se añadio a la lista: {frutas}")

print("Exercises: Level 3")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',     'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'] [len(person['skills'])//2])

    if 'Python' in person['skills']:
        print(person['skills']) 
if 'skills' in person:
    hab = person['skills']
    if 'JavaScrip'in hab and 'React'in hab:
        print('He is a front end developer')
    elif 'Node' in hab and 'Phyton'in hab and'MongoDB' in hab:
        print('He is a backed developer')
    elif 'React' in hab and 'Node' in hab and 'MongoDB' in hab:
        print('He is a fullstack developer')
    else:
        print('titulo desconocido')
        print('titulo deconocido')

if person['is_marred'] == True and 'Finland' in person['country']:
    print('Asabeneh Yetayeh vive en Finland, y es casado.')































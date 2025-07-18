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
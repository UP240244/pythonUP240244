#Exercises

dog = {}
dog['Name'] = 'Corina'
dog['Color'] = 'Blanca con manchas cafes'
dog['Breed'] = 'Bichón Maltés'
dog['Legs'] = 4
dog['Age'] = 13

student = {'First_name':'Alison Tamara', 'Last_name':'Romo Rodríguez', 'Gender':'Female', 'Age':'18', 'Marital status':'Single', 'Skills':['Crochet', 'Programación'], 'Country':'México', 'City':'Aguascachondas', 'Address':'Street Hermanos Galeana'}
print(len(student))
print(type(student['Skills']))
student['Skills'].append('Dibujo')
student['Skills'].append('Redacción')
print(student.keys())
print(student.values())
print(student.items())
del dog['Age']
del student


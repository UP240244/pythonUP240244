#Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Alphabet', 'Nvidia', 'Improving', 'Codesase'])
print(it_companies)
it_companies.remove('Nvidia')
print(it_companies)

#si deseas remover un elemento de un set usando .remove y el elemento no existe te marcara algun tipo de error
#lo contrario a .discard, pues esta función si no encuentra el elemento dejara el set tal y como esta

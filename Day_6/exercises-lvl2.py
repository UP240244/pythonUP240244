fruits=('Mandarina', 'Fresa', 'Mango', 'Piña')
vegetables=('Zanahoria', 'Papa', 'Pepino', 'Jitomate')
animal_products=('Leche', 'Queso', 'Salchicha', 'Tocino')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
food_stuff_lt.pop(6)
food_stuff_lt.pop(5)
print(food_stuff_lt)
food_stuff_lt=food_stuff_lt[3:7]
print(food_stuff_lt)
del food_stuff_tp
nordic_countries=('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
exist='Estonia' in nordic_countries
print(exist)
exist='Iceland' in nordic_countries
print(exist)
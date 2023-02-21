dictionary = {
    'ha noi': 1,
    'hai duong': 2,
    'hai phong': 3
}

for city, number in dictionary.items():
    print(f'{city.title()} city is number {number}')

print('\nCities')
for city in dictionary:
    print(city)

print('\nNumbers')
for number in dictionary.values():
    print(number)

cities = ['ha noi', 'bac ninh', 'sai gon', 'hai duong']

print()
for city in cities:
    if city in dictionary.keys():
        print(f'{city.title()} is already exist')

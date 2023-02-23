from random import choices, sample

numbers = list(range(10))
letters = ['a', 'b', 'c', 'd', 'e']
series = numbers + letters

prize = choices(series, k=4)
print(f'Any ticket matching 4 characters wins a prize')
print(f'{prize[0]} {prize[1]} {prize[2]} {prize[3]}')

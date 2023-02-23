from random import choices, sample

numbers = list(map(str, range(10)))
letters = ['a', 'b', 'c', 'd', 'e']
series = numbers + letters

my_ticket = ['1c2a', '45cc', '8412', '95cb', '9ac1', '4a5b', '6c5a']
cnt = 0

while True:
    prize = choices(series, k=4)
    prize = ''.join(prize)
    cnt += 1

    if prize in my_ticket:
        print(f'The prize is {prize}')
        break

print(f'After {cnt} times, you finally win a prize')

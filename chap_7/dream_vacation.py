vacations = []

while True:
    vacation = input(
        'If you could visit one place in the world, where would you go? (Enter quit to exit): ')
    if vacation == 'quit':
        print('❌ Quit')
        break

    vacations.append(vacation)
    print('✅ Done')

print()
for vacation in vacations:
    print(vacation)

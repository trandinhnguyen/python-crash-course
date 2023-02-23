print("Calculate sum of 2 numbers")

while True:
    print("Enter 2 numbers")
    print('Enter quit to exit')

    number_1 = input()
    if number_1 == 'quit':
        break

    number_2 = input()
    if number_1 == 'quit':
        break

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print('You must enter the number, not string')
    else:
        print(number_1 + number_2)

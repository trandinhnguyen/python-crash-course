user_names = ['admin', 'nguyen', 'tran', 'dinh', 'khoi']

# user_names.clear()

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print('hello admin, would you like to see a status report?\n')
        else:
            print(f'hello {user_name}, thank you for logging in again\n')
else:
    print('We need to find some users')

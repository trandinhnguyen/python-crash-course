current_users = ['Tran', 'Dinh', 'Nguyen', 'Anh', 'Van']

new_users = ['TRAN', 'Le', 'vu', 'Vo', 'nguyen']

lower_case = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in lower_case:
        print(
            f'This username "{new_user}" is already exist. Please enter new username\n')
    else:
        print(f'The username "{new_user}" is available\n')

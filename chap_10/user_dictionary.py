from pathlib import Path
import json


def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        try:
            user = json.loads(contents)
        except:
            print(f'{path} is empty')
            return None
        else:
            return user
    else:
        return None


def get_new_user(path):
    info = {}
    info['first_name'] = input('Enter your first name: ')
    info['middle_name'] = input('Enter your middle name: ')
    info['last_name'] = input('Enter your last name: ')

    contents = json.dumps(info)
    path.write_text(contents)


def greet_user(path):
    path = Path(path)
    user = get_stored_user(path)

    if user:
        first, middle, last = user['first_name'], user['middle_name'], user['last_name']
        print(f'Your name is {first.title()} {middle.title()} {last.title()}')
    else:
        get_new_user(path)


if __name__ == '__main__':
    path = 'text/user_info.json'
    greet_user(path)
    greet_user(path)

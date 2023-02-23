from pathlib import Path
import json


def save(path):
    try:
        number = int(input('Enter your favorite number: '))
    except ValueError:
        print('You must enter a number')
    else:
        number = json.dumps(number)
        path.write_text(number)


def get(path):
    if path.exists():
        contents = path.read_text()
        try:
            number = json.loads(contents)
        except:
            print(f'{path} is empty')
            return None
        else:
            return number
    else:
        return None


def favorite_number(path):
    path = Path(path)
    number = get(path)
    if number:
        print(f'I know your favorite number is {number}')
    else:
        save(path)


if __name__ == '__main__':
    path = 'text/favorite_number.json'
    favorite_number(path)
    favorite_number(path)

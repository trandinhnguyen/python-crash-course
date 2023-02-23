from pathlib import Path

cats_path = Path('text/cats.txt')
dogs_path = Path('text/dogs.txt')

try:
    cats = cats_path.read_text()

except FileNotFoundError:
    pass
else:
    print(cats)


try:

    dogs = dogs_path.read_text()
except FileNotFoundError:
    print(f'The {dogs_path} file is not exist')
else:

    print(dogs)

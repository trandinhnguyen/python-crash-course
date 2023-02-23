from pathlib import Path

path = Path('text/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

birthday = input('Enter your birthday (ddmmyy): ')
if birthday in pi_string:
    print('YES')
else:
    print('NO')

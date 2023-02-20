origin = [1, 2, 3, 4, 5]

new = origin  # the new list will reference the old list
new.append(6)
print('\nOrigin', origin)
print('New', new)

new = origin[:]  # must use slice to copy a list
new.append(7)
print("\nOrigin", origin)
print("new", new)

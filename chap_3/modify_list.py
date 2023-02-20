names = ['tran', 'dinh', 'nguyen', 'car', 'bike', 'bus']
print(names)


# ADD
print('\nStarting add')
names.insert(0, 'plane')  # add to index
print(names)

names.insert(4, 'motorbike')
print(names)

names.append('train')  # add to end
print(names)


# REMOVE
print('\nStarting remove')
del names[0]  # remove with index
print(names)

popped = names.pop(0)  # pop() return value, default is index -1
print(names, popped)

popped = names.pop()
print(names, popped)

names.append('nguyen')
names.remove('nguyen')  # remove the first occurrence
print(names)

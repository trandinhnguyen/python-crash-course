places = ['ha noi', 'hai duong', 'hai phong', 'sai gon', 'quang ninh',
          'quang ngai', 'quang nam', 'ha nam', 'bac ninh', 'bac giang', 'phu tho']

print(places)

print('\nSort without change origin')
new_list = sorted(places)  # sort list temporarily with sorted() func
print('new', new_list)
print('origin', places)

new_list = sorted(places, reverse=True)
print('\nnew', new_list)
print('origin', places)

print('\nReverse list')
places.reverse()
print('origin after reverse', places)
places.reverse()
print('origin after reverse again', places)

print('\nSort permanently with sort() method')
places.sort()
print('origin after sort', places)
places.sort(reverse=True)
print('after sort and reverse', places)

print('\nLength:', len(places))

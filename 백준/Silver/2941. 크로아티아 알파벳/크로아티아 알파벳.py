s = input()

lists = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = 0
tmp = s[:]

for elem in lists:
    if elem in s:
        result += s.count(elem)
        s = s.replace(elem, '_')

for elem in s:
    if elem != '_':
        result += 1
        
print(result)

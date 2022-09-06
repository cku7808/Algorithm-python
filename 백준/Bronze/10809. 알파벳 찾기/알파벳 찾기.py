s = input()
result = []
alpha = 'abcdefghijklmnopqrstuvwxyz'

for elem in alpha:
    result.append(s.find(elem))
    
for elem in result:
    print(elem, end=" ")

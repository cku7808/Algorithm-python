s = input()
s = s.upper()
tmp = ''
num = []
max_num = 0
for elem in s:
    if elem not in tmp:
        tmp += elem
        num.append(s.count(elem))

        if s.count(elem) > max_num:
            max_num = s.count(elem)

if num.count(max(num)) > 1:
    print('?')
else:
    r = tmp[num.index(max(num))]
    print(r.upper())

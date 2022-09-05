n = int(input())
cnt = 0

if n < 10:
    result = n*10
else:
    result = n
s2 = str(result)
tmp2 = result

while cnt == 0 or int(s2) != tmp2:
    tmp = 0
    for elem in s2:
        tmp += int(elem)
    s1 = str(tmp)
    result = s2[-1] + s1[-1]
    s2 = result
    
    cnt += 1
print(cnt)

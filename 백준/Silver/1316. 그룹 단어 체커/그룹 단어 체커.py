n = int(input())

def isGroup(s):
    flag = True
    for elem in s:
        if flag == False:
            break
        if s.count(elem) != 1:
            num = s.count(elem)
            loc = s.find(elem)
            for i in range(1,num):
                if s[loc] != s[loc+i]:
                    flag = False
                    break
    return flag

ans = 0
for _ in range(n):
    s = input()
    result = isGroup(s)
    if result:
        ans += 1

print(ans)

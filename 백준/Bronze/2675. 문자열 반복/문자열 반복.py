t = int(input())

for _ in range(t):
    r,s = input().split()
    r = int(r)
    result = ''
    for elem in s:
        result += elem*r
    print(result)
        


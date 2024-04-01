import sys

a, b = map(int, sys.stdin.readline().split())

cnt = 0
while a < b:
    if b%2 == 0:
        b = b//2
    elif str(b)[-1] == "1":
        b = int(str(b)[:-1])
    else:
        break
    cnt += 1

if a == b:
    print(cnt+1)
else:
    print(-1)

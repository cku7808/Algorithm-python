import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

flag = True
for i in range(n0,101):
    if a1 * i + a0 > c * i:
        flag = False
        break
print(1 if flag else 0)

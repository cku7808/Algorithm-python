import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
answer = 0

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    answer += a*b
if x == answer:
    print("Yes")
else:
    print("No")
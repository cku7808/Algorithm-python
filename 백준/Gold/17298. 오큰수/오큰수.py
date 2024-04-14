import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

nge = [-1]*n

stack = deque()

for i in range(n):
    while stack and stack[-1][1]<a[i]:
        idx, elem = stack.pop()
        nge[idx] = a[i]
    stack.append((i, a[i]))
print(*nge)

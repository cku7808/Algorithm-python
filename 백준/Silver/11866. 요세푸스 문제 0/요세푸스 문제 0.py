import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque(list(range(1,n+1)))
result = []
cnt = 1

while q:
    cur = q.popleft()
    if cnt == k:
        result.append(cur)
        cnt = 1
    else:
        cnt += 1
        q.append(cur)

print("<"+", ".join(map(str,result))+">")

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

arr = deque([i for i in range(1,n+1)])
cnt = 1
ans = []

while len(arr)>1:
    cur = arr.popleft()
    
    if cnt == k:
        ans.append(cur)
        cnt = 1
    else:
        arr.append(cur)
        cnt += 1
ans.append(arr.pop())

print("<"+", ".join(map(str, ans))+">")

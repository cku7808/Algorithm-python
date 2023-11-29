import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

grid = [0] * 100001
visited = [False] * 100001

q = deque()
q.append(n)
visited[n] = True

while q:
    x = q.popleft()
    if x == k:
        print(grid[k])
        break
    for nx in [x*2, x-1, x+1]:
        if 0 <= nx <= 100000 and not visited[nx]:
            if nx == x*2 and nx != 0:
                grid[nx] = grid[x]
                q.appendleft(nx)
            else:
                grid[nx] = grid[x]+1
                q.append(nx)
            visited[nx] = True
                

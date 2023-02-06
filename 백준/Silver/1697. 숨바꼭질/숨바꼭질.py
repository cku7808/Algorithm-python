import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

grid = [0]*100001
visited = [False]*100001

q = deque([n])
visited[n] = True

while q:
    cur = q.popleft()

    nxs = [cur-1, cur+1, 2*cur]

    for nx in nxs:
        if 0<=nx<=100000 and not visited[nx]:
            grid[nx] = grid[cur] + 1
            visited[nx] = True
            q.append(nx)
        
print(grid[k])


import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())

graph = []

for _ in range(h):
    g = []
    for _ in range(n):
        g.append(list(map(int, sys.stdin.readline().split())))
    graph.append(g)

q = deque()

dxs = [-1,1,0,0,0,0]
dys = [0,0,-1,1,0,0]
dzs = [0,0,0,0,-1,1]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] >= 1:
                q.append((i,j,k))

while q:
    x,y,z = q.popleft()
        
    for dx,dy,dz in zip(dxs,dys,dzs):
        nx, ny, nz = dx+x, dy+y, dz+z
        if 0<=nx<=n-1 and 0<=ny<=m-1 and 0<=nz<=h-1:
            if graph[nz][nx][ny] == 0:
                q.append((nx,ny,nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1

ans = 0           
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans,max(j))
print(ans-1)
                    
    

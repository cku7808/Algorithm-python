import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(sys.stdin.readline().strip())

visited = [[False]*n for _ in range(n)]

def bfs(i,j):
    cnt = 0
    if visited[i][j]:
        return 0

    q = deque([(i,j)])
    
    visited[i][j] = True

    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    while q:
        x,y = q.popleft()
        cnt += 1
        
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
                
                if graph[nx][ny] != "0" and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != "0":
            num = bfs(i,j)
            if num > 0:
                result.append(num)

result.sort()
print(len(result))
for elem in result:
    print(elem)
            
    

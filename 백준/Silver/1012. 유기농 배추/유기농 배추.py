import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(i,j,visited):
    if visited[i][j]:
        return 0

    cnt = 0
    q = deque([(i,j)])
    visited[i][j] = True

    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    while q:
        x,y = q.popleft()
        cnt += 1
        for dx, dy in zip(dxs,dys):
            nx,ny = dx+x, dy+y

            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return cnt

for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())

    graph = [[False]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for _ in range(k):
        y,x = tuple(map(int, sys.stdin.readline().split()))
        graph[x][y] = True
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and visited[i][j]==False:
                cnt = 0
                q = deque([(i,j)])
                visited[i][j] = True

                dxs = [-1,1,0,0]
                dys = [0,0,-1,1]
    
                while q:
                    x,y = q.popleft()
                    cnt += 1
                    for dx, dy in zip(dxs,dys):
                        nx,ny = dx+x, dy+y

                        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                            if graph[nx][ny] and not visited[nx][ny]:
                                q.append((nx,ny))
                                visited[nx][ny] = True
                if cnt > 0:
                    ans += 1
    print(ans)
    

    

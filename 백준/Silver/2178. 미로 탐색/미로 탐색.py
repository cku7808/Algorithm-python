import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(sys.stdin.readline().strip())

visited = [[0]*m for _ in range(n)]


dxs = [-1,1,0,0]
dys = [0,0,-1,1]

q = deque()
q.append((0,0))
visited[0][0] = 1

while q:
    x,y = q.popleft()

    for dx, dy in zip(dxs,dys):
        nx, ny = dx+x, dy+y
        if -1<nx<n and -1<ny<m:
            if not visited[nx][ny] and graph[nx][ny] == "1":
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
print(visited[n-1][m-1])
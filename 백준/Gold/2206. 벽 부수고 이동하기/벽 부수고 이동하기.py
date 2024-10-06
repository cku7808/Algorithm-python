import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def bfs(x, y, z):
    q = deque([(x, y, z)])
    visited[x][y][z] = 1

    while q:
        x, y, check = q.popleft()

        if (x, y) == (n-1, m-1):
            return visited[x][y][check]

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if -1<nx<n and -1<ny<m:
                if graph[nx][ny] == "0" and not visited[nx][ny][check]:
                    visited[nx][ny][check] = visited[x][y][check] + 1
                    q.append((nx, ny, check))
                if graph[nx][ny] == "1" and check == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
    return -1

print(bfs(0, 0, 0))
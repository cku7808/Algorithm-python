from collections import deque

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = 0
pic_num = 0

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            pic_num += 1
            cnt = 1
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = dx+x, dy+y
                    if -1 < nx < n and -1 < ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                        cnt += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
            ans = max(ans, cnt)
print(pic_num)
print(ans)
import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def bfs(a,b):
    q = deque()
    tmp = []
    q.append((a,b))
    tmp.append((a,b))

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y

            if -1<nx<n and -1<ny<n and not visited[nx][ny]:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    q.append((nx,ny))
                    tmp.append((nx,ny))
                    visited[nx][ny] = True
    return tmp

cnt = 0
while True:
    visited = [[False]*n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                result = bfs(i,j)
                if len(result) > 1:
                    flag = 1
                    num = sum([arr[x][y] for x,y in result]) // len(result)

                    for x,y in result:
                        arr[x][y] = num
    if not flag:
        break
    cnt += 1
print(cnt)
        

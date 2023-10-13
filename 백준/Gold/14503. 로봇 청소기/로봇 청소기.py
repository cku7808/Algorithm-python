import sys

n,m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

cleaned = [[False]*m for _ in range(n)]

x, y = r, c

ans = 1
cleaned[x][y] = True

while True:
    flag = False
    for _ in range(4):
        nx, ny = dxs[(d-1+4)%4]+x, dys[(d-1+4)%4]+y
        if -1<nx<n and -1<ny<m and grid[nx][ny] == 0 and not cleaned[nx][ny]:
            d = (d-1+4)%4
            x, y = nx, ny
            cleaned[x][y] = True # 청소
            ans += 1
            flag = True
            break
        else:
            d = (d-1+4)%4
    if not flag:
        nx, ny = dxs[(d-1+3)%4]+x, dys[(d-1+3)%4]+y
        if grid[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
        
        
print(ans)

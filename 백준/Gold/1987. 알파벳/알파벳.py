import sys

r,c = map(int, sys.stdin.readline().split())
grid = []

for _ in range(r):
    grid.append(list(sys.stdin.readline().strip()))


dxs = [-1,1,0,0]
dys = [0,0,-1,1]

check = [False]*27

ans = 0

def dfs(grid, x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if -1<nx<r and -1<ny<c and not check[ord(grid[nx][ny])-64]:
            check[ord(grid[nx][ny])-64] = True
            dfs(grid, nx, ny, cnt+1)
            check[ord(grid[nx][ny])-64] = False

check[ord(grid[0][0])-64] = True
dfs(grid, 0, 0, 1)
print(ans)    

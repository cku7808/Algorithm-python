import sys

n, m = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dxs = [-1,1,0,0]  
dys = [0,0,-1,1]

visited = [[False]*m for _ in range(n)]

# dfs를 사용하되 호출 횟수를 4번으로 제한(백트래킹)
def dfs(x, y, cnt, result):
    global local_max
    if cnt == 4:
        local_max = max(local_max, result)
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if -1<nx<n and -1<ny<m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = True
                result += grid[nx][ny]
                dfs(x, y, cnt+1, result)
                visited[nx][ny] = False
                result -= grid[nx][ny]
            visited[nx][ny] = True
            result += grid[nx][ny]
            dfs(nx, ny, cnt+1, result)
            visited[nx][ny] = False
            result -= grid[nx][ny]

global_max = 0
for i in range(n):
    for j in range(m):
        local_max = 0
        result = grid[i][j]
        visited[i][j] = True
        dfs(i, j, 1, result)
        global_max = max(global_max, local_max)
        visited[i][j] = False

print(global_max)

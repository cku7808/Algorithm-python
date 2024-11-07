import sys
input = sys.stdin.readline

# 0 : 가로, 1 : 세로, 2 : 대각선
dxs = [0, 1, 1]
dys = [1, 0, 1]

dirs = {
    0 : [0, 2],
    1 : [1, 2],
    2 : [0, 1, 2]
}

def DFS(x, y, dir):
    global cnt
    visited[x][y] = True

    for idx in dirs[dir]:
        nx, ny = x+dxs[idx], y+dys[idx]
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue
        if graph[nx][ny] == 1 or visited[nx][ny]:
            continue
        if idx == 2 and 1 in [graph[x][y+1], graph[x+1][y]]:
            continue
        if (nx, ny) == (dest_x, dest_y):
            cnt += 1
            return
        DFS(nx, ny, idx)
        visited[nx][ny] = False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = 0, 1
dest_x, dest_y = n-1, n-1
cnt = 0
visited = [[False]*n for _ in range(n)]
visited[0][0] = True
if graph[dest_x][dest_y] == 1:
    print(0)
else:
    DFS(start_x, start_y, 0)
    print(cnt)
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dxs = [0,0,1,-1]
    dys = [1,-1,0,0]

    max_num = 0
    for i in range(n):
        for j in range(m):
            num = grid[i][j]
            for dx, dy in zip(dxs, dys):
                nx, ny = dx+i, dy+j
                if -1 < nx < n and -1 < ny < m:
                    num += grid[nx][ny]
            max_num = max(num, max_num)

    print(f"#{tc} {max_num}")
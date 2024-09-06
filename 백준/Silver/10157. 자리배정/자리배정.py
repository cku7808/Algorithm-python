C, R = map(int, input().split())
K = int(input())

graph = [[0] * C for _ in range(R)]
visited = [0] * (C*R+1)
if K > R*C:
    print(0)
else:
    # 하 우 상 좌
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    i, j, dir = 0, 0, 0
    for num in range(1, R*C+1):
        graph[i][j] = num
        new_y = i + dy[dir]
        new_x = j + dx[dir]
        visited[num] = (i+1, j+1)
        if new_y < 0 or new_y >= R or new_x < 0 or new_x >= C or graph[new_y][new_x]:
            dir = (dir+1) % 4

        i += dy[dir]
        j += dx[dir]

    print(visited[K][1], visited[K][0])
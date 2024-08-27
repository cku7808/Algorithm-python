import sys
from collections import deque

t = int(input())

for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
    time = 0
    pos_x, pos_y = 0, 0
    fire = deque()

    # 시작 위치, 불 위치 찾기
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                pos_x, pos_y = i, j
            elif graph[i][j] == "*":
                fire.append((i, j))

    # 탐색
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    visited = [[0]*w for _ in range(h)]
    pos_q = deque([(pos_x, pos_y)])
    visited[pos_x][pos_y] = 1

    while pos_q:

        fire_len = len(fire)
        for _ in range(fire_len):
            fx, fy = fire.popleft()
            for dx, dy in zip(dxs, dys):
                # 불이 옮겨붙기
                fnx, fny = dx + fx, dy + fy
                if -1 < fnx < h and -1 < fny < w and graph[fnx][fny] != "#" and graph[fnx][fny] != "*":
                    graph[fnx][fny] = "*"
                    fire.append((fnx, fny))

        pos_len = len(pos_q)
        for _ in range(pos_len):
            x, y = pos_q.popleft()
            for dx, dy in zip(dxs, dys):
                # 불이 없는 곳으로 이동하기
                nx, ny = dx + x, dy + y
                if -1 < nx < h and -1 < ny < w and not visited[nx][ny] and graph[nx][ny] == ".":
                    visited[nx][ny] = visited[x][y] + 1
                    pos_q.append((nx, ny))

    ans = sys.maxsize
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1:
                if visited[i][j] != 0:
                    ans = min(visited[i][j], ans)
            if j == 0 or j == w-1:
                if visited[i][j] != 0:
                    ans = min(visited[i][j], ans)

    if ans == sys.maxsize:
        print("IMPOSSIBLE")
    else:
        print(ans)
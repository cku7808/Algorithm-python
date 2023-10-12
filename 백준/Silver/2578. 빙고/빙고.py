import sys

grid = []
for _ in range(5):
    grid.append(list(map(int, sys.stdin.readline().split())))

cmd = []
for _ in range(5):
    cmd.extend(list(map(int, sys.stdin.readline().split())))

# 빙고체크
def check(grid):
    cnt = 0
    # 가로
    for i in range(5):
        if sum(grid[i]) == 0:
            cnt += 1
    # 세로
    for i in range(5):
        vert = 0
        for j in range(5):
            vert += grid[j][i]
        if vert == 0:
            cnt += 1
    # 대각
    left = 0
    right = 0
    for i in range(5):
        left += grid[i][i]
        right += grid[i][-(i+1)]
    if left == 0:
        cnt += 1
    if right == 0:
        cnt += 1
    return cnt

# 위치 저장
pos = {}
for i in range(5):
    for j in range(5):
        if str(grid[i][j]) not in pos:
            pos[str(grid[i][j])] = (i,j)
        

for idx, num in enumerate(cmd):
    x,y = pos[str(num)]
    grid[x][y] = 0
    cnt = check(grid)
    if cnt >= 3:
        print(idx+1)
        break
    

    

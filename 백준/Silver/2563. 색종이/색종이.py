import sys

n = int(sys.stdin.readline())
grid = [[0]*100 for _ in range(100)]

for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())

    for i in range(x,x+10):
        for j in range(y, y+10):
            if grid[i][j] == 0:
                grid[i][j] = 1
ans = 0
for i in range(len(grid)):
    ans += sum(grid[i])
print(ans)

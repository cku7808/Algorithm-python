import sys
n,m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))

prefix = grid[:]

for i in range(n):
    for j in range(1,n):
        prefix[i][j] += prefix[i][j-1]

for _ in range(m):
    x,y,a,b = map(int, sys.stdin.readline().split())
    x,y,a,b = x-1,y-1,a-1,b-1
    result = 0
    for i in range(x,a+1):
        if y!=0:
            result += grid[i][b] - grid[i][y-1]
        else:
            result += grid[i][b]
    print(result)

        
        

import sys
arr1 = sys.stdin.readline().strip()
arr2 = sys.stdin.readline().strip()

n = len(arr1)
m = len(arr2)
grid = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr1[i-1] == arr2[j-1]:
            grid[i][j] = grid[i-1][j-1]+1
        else:
            grid[i][j] = max(grid[i-1][j],grid[i][j-1])
print(grid[n][m])

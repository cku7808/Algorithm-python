import sys

n,m,k = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().strip())
value = grid[0][0] != "W"

def board(color):
    prefix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i+j)%2 == 0:
                value = grid[i][j] != color
            else:
                value = grid[i][j] == color
            prefix[i+1][j+1] = prefix[i][j+1]+prefix[i+1][j] - prefix[i][j] + value
            
    count = sys.maxsize
    for i in range(1,n-k+2):
        for j in range(1,m-k+2):
            count = min(count, prefix[i+k-1][j+k-1]-prefix[i+k-1][j-1]-prefix[i-1][j+k-1]+prefix[i-1][j-1])
    return count        

print(min(board("B"), board("W")))

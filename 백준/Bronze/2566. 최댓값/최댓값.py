import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

ans = 0
pos = (0,0)

for i in range(9):
    for j in range(9):
        if arr[i][j] > ans:
            ans = arr[i][j]
            pos = (i,j)
print(ans)
print(pos[0]+1, pos[1]+1)

import sys

def count(a,b,grid):
    if a+8 > n or b+8 > m:
        return sys.maxsize
    cnt1 = 0
    cnt2 = 0
    tmp = [row[b:b+8] for row in grid[a:a+8]]

    bstart = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
    wstart = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]

    start = tmp[0][0]
    for i in range(8):
        for j in range(8):
            if tmp[i][j] != bstart[i][j]:
                cnt1 += 1
    for i in range(8):
        for j in range(8):
            if tmp[i][j] != wstart[i][j]:
                cnt2 += 1
    return min(cnt1,cnt2)
        
n,m = map(int,sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().strip())

ans = sys.maxsize
for i in range(n):
    for j in range(m):
        tmp = count(i,j,grid)
        if ans > tmp:
            ans = tmp
print(ans)

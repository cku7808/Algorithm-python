import sys
grid = []
for _ in range(9):
    grid.append(list(map(int, sys.stdin.readline().split())))

zero = [(i,j) for i in range(9) for j in range(9) if grid[i][j]==0]

def checker1(i,k): #가로줄 확인
    for n in range(9):
        if grid[i][n] == k:
            return False
    return True

def checker2(j,k): #세로줄 확인
    for n in range(9):
        if grid[n][j] == k:
            return False
    return True

def checker3(i,j,k): #3*3 확인
    nx = i//3*3
    ny = j//3*3

    for n in range(3):
        for m in range(3):
            if k == grid[nx+n][ny+m]:
                return False
    return True

def sdoku(cnt):
    if cnt == len(zero):
        for elem in grid:
            print(*elem)
        exit(0)
    else:
        for k in range(1,10):
            x = zero[cnt][0]
            y = zero[cnt][1]
     
            if checker1(x,k) and checker2(y,k) and checker3(x,y,k):
                grid[x][y] = k
                sdoku(cnt+1)
                grid[x][y] = 0

sdoku(0)


            

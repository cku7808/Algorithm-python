import sys
n = int(sys.stdin.readline())

grid = [0]*n
cnt = 0
ans = 0

def check(cnt): #이전 열의 값과의 비교(같은 열/행은아닌지, 대각선에 있는 값은 아닌지)
    for i in range(cnt):
        if grid[cnt]==grid[i] or abs(grid[cnt]-grid[i])==abs(cnt-i):
            return False
    return True

def nqueen(cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    else:
        for i in range(n):
            grid[cnt] = i
            if check(cnt):
                nqueen(cnt+1)
nqueen(0)
print(ans)
            
            
                

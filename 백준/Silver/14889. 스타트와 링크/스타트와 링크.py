import sys
n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

selected = [False]*n
ans = 1e9

def sol(cnt, idx):
    global ans
    if cnt == n//2:
        team1, team2 = 0,0
        for i in range(n):
            for j in range(i+1,n):
                if selected[i] and selected[j]:
                    team1 += (grid[i][j]+grid[j][i])
                elif not selected[i] and not selected[j]:
                    team2 += (grid[i][j]+grid[j][i])
        ans = min(ans, abs(team1-team2))
    for i in range(idx,n):
        if not selected[i]:
            selected[i] = True
            sol(cnt+1, i+1)
            selected[i] = False


sol(0,0)
print(ans)

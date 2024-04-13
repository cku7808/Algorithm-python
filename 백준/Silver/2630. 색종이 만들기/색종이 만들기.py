import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []

def slicing(x,y,n):
    color = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                slicing(x, y, n//2)
                slicing(x+n//2, y, n//2)
                slicing(x, y+n//2, n//2)
                slicing(x+n//2, y+n//2, n//2)
                return
    result.append(color)

slicing(0,0,n)
print(result.count(0))
print(result.count(1))
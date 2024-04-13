import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []

def slicing(x,y,n):
    cur = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if cur != graph[i][j]:
                slicing(x, y, n//3)
                slicing(x, y+n//3, n//3)
                slicing(x, y+n//3*2, n//3)

                slicing(x+n//3, y, n//3)
                slicing(x+n//3, y+n//3, n//3)
                slicing(x+n//3, y+n//3*2, n//3)

                slicing(x+n//3*2, y, n//3)
                slicing(x+n//3*2, y+n//3, n//3)
                slicing(x+n//3*2, y+n//3*2, n//3)
                return
    result.append(cur)

slicing(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
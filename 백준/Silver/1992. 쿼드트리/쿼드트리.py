import sys

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)]
answer = ""
def slicing(x,y,n):
    global answer

    cur = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != cur:
                answer += "("
                slicing(x, y, n//2)
                slicing(x, y+n//2, n//2)
                slicing(x+n//2, y, n//2)
                slicing(x+n//2, y+n//2, n//2)
                answer += ")"
                return
    answer += cur

slicing(0,0,n)
print(answer)
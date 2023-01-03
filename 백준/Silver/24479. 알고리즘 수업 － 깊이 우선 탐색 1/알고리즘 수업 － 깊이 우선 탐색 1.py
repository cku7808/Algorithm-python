import sys
sys.setrecursionlimit(10**9)
n,m,r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
order = [0]*(n+1)
cnt = 1

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    global cnt
    visited[v] = True
    order[v] = cnt
    graph[v].sort()
    for elem in graph[v]:
        if visited[elem] == False:
            cnt += 1
            DFS(elem)


DFS(r)
print(*order[1:], sep="\n")

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = float("inf")
graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    v, u, w = map(int, sys.stdin.readline().split())
    graph[v][u] = min(w, graph[v][u])

for i in range(1, v+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0

for arr in graph[1:]:
    print(*arr[1:])

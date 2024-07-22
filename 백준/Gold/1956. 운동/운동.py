import sys, heapq

v, e = map(int, sys.stdin.readline().split())

inf = float("inf")
graph = [[inf]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for i in range(1, v+1):
    if graph[i][i] == inf:
        graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

min_num = inf

for i in range(1, v+1):
    if graph[i][i] == 0:
        graph[i][i] = inf
            
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            min_num = min(graph[i][j], min_num)
        else:
            min_num = min(graph[i][j] + graph[j][i], min_num)

if min_num == inf:
    print(-1)
else:
    print(min_num)

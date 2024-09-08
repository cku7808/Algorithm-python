import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float("inf")
graph = [[inf]*(n+1) for _ in range(n+1)]
route = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])
    route[a][b] = b

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                route[i][j] = route[i][k]
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0

for elem in graph[1:]:
    print(*elem[1:])

for i in range(1, n+1):
    for j in range(1, n+1):
        if route[i][j] == inf:
            print(0)
        else:
            pointer = i
            tmp = [i]
            while route[pointer][j] != j:
                tmp.append(route[pointer][j])
                pointer = route[pointer][j]
            tmp.append(j)
            print(len(tmp), *tmp)
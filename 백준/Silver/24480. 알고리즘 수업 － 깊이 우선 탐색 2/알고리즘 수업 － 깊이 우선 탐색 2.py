import sys
sys.setrecursionlimit(10000000)
n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
order = [0]*(n+1)
cnt = 1

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def DFS(graph, v, visited):
    global cnt
    visited[v] = True
    order[v] = cnt
    graph[v].sort()
    graph[v].reverse()
    for elem in graph[v]:
        if visited[elem] == False:
            cnt += 1
            DFS(graph, elem, visited)

DFS(graph, r, visited)
for elem in order[1:]:
    print(elem)

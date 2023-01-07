import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

def DFS(graph, v, visited):
    global cnt
    
    visited[v] = True
    
    for elem in graph[v]:
        if visited[elem] == False:
            cnt += 1
            DFS(graph, elem, visited)
DFS(graph,1,visited)
print(cnt)
    

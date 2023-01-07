import sys
n,m,s = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=" ")
    graph[v].sort()
    for elem in graph[v]:
        if not visited_dfs[elem]:
            dfs(graph, elem, visited_dfs)

def bfs(graph, v, visited_bfs):
    q = [v]
    visited_bfs[v] = True

    while q:
        cur = q.pop(0)
        print(cur, end=" ")
        graph[cur].sort()
        for elem in graph[cur]:
            if visited_bfs[elem] == False:
                q.append(elem)
                visited_bfs[elem] = True

dfs(graph,s,visited_dfs)
print()
bfs(graph,s,visited_bfs)

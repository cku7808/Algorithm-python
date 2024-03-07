import sys
sys.setrecursionlimit(100000000)

n = int(sys.stdin.readline())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)

def dfs(graph, visited, start):
    visited[start] = True
    for elem in graph[start]:
        if not visited[elem]:
            dfs(graph, visited, elem)
            answer[elem] = start

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, visited, 1)
for elem in answer[2:]:
    print(elem)

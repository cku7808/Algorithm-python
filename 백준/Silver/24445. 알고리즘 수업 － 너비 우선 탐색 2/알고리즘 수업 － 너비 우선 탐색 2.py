import sys
n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
order = [0]*(n+1)
q = [r]
order[r] = 1

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
while len(q):
    cur = q.pop(0)
    visited[cur] = True
    graph[cur].sort()
    graph[cur].reverse()
    for elem in graph[cur]:
        if visited[elem] == False:
            q.append(elem)
            visited[elem] = True
            cnt += 1
            order[elem] = cnt

for elem in order[1:]:
    print(elem)

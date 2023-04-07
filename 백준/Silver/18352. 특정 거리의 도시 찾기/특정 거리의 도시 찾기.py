import sys
from collections import deque

n,m,k,x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

q = deque()

q.append(x)
visited[x] = 1
while q:
    pos = q.popleft()

    for next in graph[pos]:
        if not visited[next]:
            q.append(next)
            visited[next] = visited[pos] + 1

answer = -1
for idx, elem in enumerate(visited):
    if elem == k+1:
        answer = idx
        print(answer)
if answer == -1:
    print(-1)

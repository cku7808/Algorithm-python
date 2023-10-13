import sys
import heapq

v,e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)

for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


ans = 0
heap = [(0,1)]

while heap:
    weight, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    ans += weight

    for w, u in graph[node]:
        heapq.heappush(heap, (w,u))
print(ans)
    
    
    

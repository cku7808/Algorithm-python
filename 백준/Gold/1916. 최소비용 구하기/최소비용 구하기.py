import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = float("inf")
graph = [[] for _ in range(n+1)]
dist = [inf] * (n+1)

for _ in range(m):
    v, u, w = map(int, sys.stdin.readline().split())
    graph[v].append((u,w))

start, dest = map(int, sys.stdin.readline().split())

q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    w1, v = heapq.heappop(q)
    if dist[v] < w1:
        continue

    for u, w2 in graph[v]:
        cost = dist[v] + w2
        if dist[u] > cost:
            dist[u] = cost
            heapq.heappush(q, (cost, u))
print(dist[dest])

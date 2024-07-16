import sys, heapq

inf = float("inf")
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
dist = [inf] * (v+1)

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        w1, v = heapq.heappop(q)

        for w2, u in graph[v]:
            cost = dist[v] + w2
            if cost < dist[u]:
                dist[u] = cost
                heapq.heappush(q, (cost,u))
    
dijkstra(k)

for elem in dist[1:]:
    print(elem) if elem != inf else print("INF")

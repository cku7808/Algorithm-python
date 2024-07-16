import sys, heapq

n, e = map(int, sys.stdin.readline().split())
inf = float("inf")
graph = [[] for _ in range(n+1)]


for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start, dest):
    dist = [inf] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w1, v = heapq.heappop(q)
        if v == dest:
            return dist[dest]

        for w2, u in graph[v]:
            cost = dist[v] + w2
            if cost < dist[u]:
                dist[u] = cost
                heapq.heappush(q, (cost, u))

def calculator(start, first, final, dest):
    try:
        ans = dijkstra(start, first)+dijkstra(first, final)+dijkstra(final, dest)
    except:
        ans = float("inf")
    return ans
        
ans = min(calculator(1,v1,v2,n), calculator(1,v2,v1,n))

if ans != inf:
    print(ans)
else:
    print(-1)

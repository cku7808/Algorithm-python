import sys, heapq
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a
while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    total, result = 0, 0
    heap = []
    parent = list(range(m+1))
    for _ in range(n):
        x, y, z = map(int, input().split())
        total += z
        heapq.heappush(heap, (z, x, y))
    
    while heap:
        cost, x, y = heapq.heappop(heap)
    
        if find(x) != find(y):
            union(x, y)
            result += cost
    print(total - result)
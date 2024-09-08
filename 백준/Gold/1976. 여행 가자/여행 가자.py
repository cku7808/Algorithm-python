import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    info = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if info[j]:
            union(i, j+1)

route = list(map(int, sys.stdin.readline().split()))
ans = "YES"
for i in range(m-1):
    if parent[route[i]] != parent[route[i+1]]:
        ans = "NO"
        break
print(ans)
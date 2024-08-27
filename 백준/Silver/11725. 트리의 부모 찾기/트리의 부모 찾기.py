import sys
sys.setrecursionlimit(10**6)

def func(node):

    for w in adjl[node]:

        if visited[w] == 1:
            continue
        visited[w] = 1
        func(w)
        parent[w] = node



N = int(sys.stdin.readline())
adjl = [[] for _ in range(N+1)]
for _ in range(N-1):
    arr = sys.stdin.readline().split()
    i, j = int(arr[0]), int(arr[1])
    adjl[i].append(j)
    adjl[j].append(i)

parent = [0] * (N+1)
visited = [0] * (N+1)
func(1)
for idx in range(2, N+1):
    print(parent[idx])
import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(x):
    q = deque()
    q.append(x)
    color[x] = 1

    while q:
        pos = q.popleft()
        visited[pos] = True

        for elem in linkedlist[pos]:
            if not visited[elem]:
                color[elem] = -color[pos]
                visited[elem] = True
                q.append(elem)
            else:
                if color[elem] == color[pos]:
                    return False
    return True
                

for _ in range(k):
    v,e = map(int, sys.stdin.readline().split())
    
    linkedlist = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    color = [0]*(v+1)
    
    for _ in range(e):
        a,b = map(int, sys.stdin.readline().split())
        linkedlist[a].append(b)
        linkedlist[b].append(a)
    for i in range(1,v+1):
        if not visited[i]:
            result = bfs(i)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")


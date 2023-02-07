import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

ladder = dict()
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    ladder[a] = b

snake = dict()
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    snake[a] = b

grid = [i for i in range(101)]


cnt = [0]*101
visited = [False]*101
q = deque([1])
visited[1] = True

while q:
    x = q.popleft()
        
    for i in range(1,7):
        nx = x+i
        if 1<=nx<=100 and visited[nx]==False:
            if nx in ladder.keys():
                nx = ladder[nx]
                
            if nx in snake.keys():
                nx = snake[nx]

            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                cnt[nx] = cnt[x] + 1
                
print(cnt[100])

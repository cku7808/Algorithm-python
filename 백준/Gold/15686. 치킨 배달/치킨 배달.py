import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

home = []
chicken = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if row[j] == 1:
            home.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))

visited = [False]*len(chicken)

def select_store(idx,cnt):
    global final_ans
    if cnt == m:
        ans = 0
        for hi,hj in home:
            min_dist = 999999
            for j in range(len(chicken)):
                if visited[j]:
                    min_dist = min(abs(hi-chicken[j][0]) + abs(hj-chicken[j][1]), min_dist)
            ans += min_dist
        final_ans = min(ans, final_ans)
        return
    
    for i in range(idx,len(chicken)):
        if not visited[i]:
            visited[i] = True
            select_store(i+1, cnt+1)
            visited[i] = False
            
final_ans = 999999
select_store(0,0)
print(final_ans)

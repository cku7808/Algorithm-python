import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
visited = [False]*n

a = deque(a)
visited =deque(visited)
cnt = 0

while True:
    cnt += 1
    # 1. 회전
    tmp1 = a.pop()
    tmp2 = visited.pop()
    a.appendleft(tmp1)
    visited.appendleft(tmp2)
    
    # 내리는 위치에서 내림
    visited[n-1] = False

    # 2. 로봇 옮기는 과정
    for i in range(n-2, -1, -1):
        # 앞 칸이 비어있고 내구도가 1이상이면 이동
        if visited[i] == True and visited[i+1] == False and a[i+1] >= 1:
            visited[i] = False
            visited[i+1] = True
            a[i+1] -= 1
    visited[n-1] = False

            
    # 3. 로봇 올리기
    if a[0] >= 1 and not visited[0] :
        visited[0] = True
        a[0] -= 1
        
    # 4. 내구도가 0인 블럭 개수 점검 
    if a.count(0) >= k:
        break
    #print(a)
    #print(visited)

print(cnt)

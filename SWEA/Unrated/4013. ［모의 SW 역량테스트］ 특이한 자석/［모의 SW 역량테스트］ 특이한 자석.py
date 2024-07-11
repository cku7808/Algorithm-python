from collections import deque

t = int(input())
for i in range(1, t+1):
    k = int(input())
    lists = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(k):
        num, direction = map(int, input().split())
             
        q = deque([(num-1, direction)])
        
        visited = [False]*4
        
        while q:
            x, d = q.popleft()
            visited[x] = True
            
            if x < 3:
                if lists[x][2] != lists[x+1][6] and not visited[x+1]:
                    q.append((x+1, -d))
            if x > 0:
                if lists[x][6] != lists[x-1][2] and not visited[x-1]:
                    q.append((x-1, -d))
                      
            # 회전
            tmp = lists[x][:]

            if d == 1:
                lists[x] = [tmp[-1]]+tmp[:-1]
            else:
                lists[x] = tmp[1:]+[tmp[0]]
    score = 0
    for j in range(4):
        if lists[j][0] == 1:
            score += pow(2,j)
            
    print("#"+str(i), score)
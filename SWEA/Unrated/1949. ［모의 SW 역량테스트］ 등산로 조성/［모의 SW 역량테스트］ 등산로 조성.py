T = int(input())

dxs = [0,0,1,-1]
dys = [1,-1,0,0]
result = []

def DFS(x, y, cnt, k_cnt):
    global max_cnt

    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if -1<nx<n and -1<ny<n and not visited[nx][ny]:
            #print((x,y), (nx,ny))
            if graph[nx][ny] < graph[x][y]:
                visited[nx][ny] = True
                max_cnt = max(DFS(nx, ny, cnt+1, k_cnt), max_cnt)
                visited[nx][ny] = False
            else:
                if k_cnt == 0:
                    for i in range(1, k+1):
                        if graph[nx][ny] - i < graph[x][y]:
                        
                            graph[nx][ny] -= i
                            #print("깎")
                            visited[nx][ny] = True
                            max_cnt = max(DFS(nx, ny, cnt+1, k_cnt+1), max_cnt)
                            graph[nx][ny] += i
                            visited[nx][ny] = False
        #print(cnt)
    return cnt

for i in range(1, T+1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    # 가장 높은 봉우리 찾기
    high = []
    max_num = 0
    for j in range(n):
        max_num = max(max_num, max(graph[j]))
    
    for a in range(n):
        for b in range(n):
            if graph[a][b] == max_num:
                high.append((a, b))
                
    # DFS
    for x, y in high:
        max_cnt = 0
        visited = [[False]*n for _ in range(n)]
        visited[x][y] = True
        k_cnt = 0
        DFS(x, y, 1, k_cnt)
        ans = max(ans, max_cnt)

    print(f"#{i} {ans}")

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    q = deque([(0,0)])
    visited[0][0] = 1
    dxs = [1,-1,0,0]
    dys = [0,0,1,-1]
    
    while q:
        x,y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if -1<nx<n and -1<ny<m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    if not visited[n-1][m-1]:
        return -1
    else:
        return visited[n-1][m-1]
    return answer
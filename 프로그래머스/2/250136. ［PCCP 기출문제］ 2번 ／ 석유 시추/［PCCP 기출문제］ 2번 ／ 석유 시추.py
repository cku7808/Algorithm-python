from collections import deque
import copy

def solution(land):
    col_num = len(land[0])
    row_num = len(land)
    
    dxs = [1,-1,0,0]
    dys = [0,0,1,-1]
    
    visited = [[False]*col_num for _ in range(row_num)]
    cols_score = [0]*col_num
    
    for i in range(row_num):
        for j in range(col_num):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                cnt = 0
                cols = set()
                while q:
                    x, y = q.popleft()
                    cols.add(y)
                    cnt += 1

                    for dx, dy in zip(dxs, dys):
                        nx, ny = dx+x, dy+y
                        if -1<nx<row_num and -1<ny<col_num and land[nx][ny] == 1 and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                for idx in cols:
                    cols_score[idx] += cnt
    return max(cols_score)                
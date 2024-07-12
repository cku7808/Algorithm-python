from collections import deque
import copy

def solution(land):
    col_num = len(land[0])
    row_num = len(land)
    
    dxs = [1,-1,0,0]
    dys = [0,0,1,-1]
    
    # bfs로 석유 위치와 석유 덩어리 크기 구하기
    pos_list = []
    cnt = 2
    for i in range(row_num):
        for j in range(col_num):
            tmp = []
            if land[i][j] == 1:
                q = deque([(i,j)])
                tmp.append((i,j))
                land[i][j] = cnt
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = dx+x, dy+y
                        if -1<nx<row_num and -1<ny<col_num and land[nx][ny] == 1:
                            q.append((nx, ny))
                            tmp.append((nx, ny))
                            land[nx][ny] = cnt

            if len(tmp):
                pos_list.append(tmp)
                cnt += 1

    # 석유 덩어리 크기를 저장하기
    size = dict()
    for i in range(2, cnt):
        size[i] = len(pos_list[i-2])

    # 열 별로 순회하며 얻을 수 있는 석유 덩어리들의 크기를 더하기 
    # transpose and summation
    max_amount = 0
    for elem in zip(*land):
        tmp = 0
        for num in set(elem):
            if num != 0:
                tmp += size[num]
        max_amount = max(tmp, max_amount)
    return max_amount
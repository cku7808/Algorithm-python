# from collections import deque

# def solution(n, computers):
#     answer = 0
    
#     dxs = [0,0,1,-1]
#     dys = [1,-1,0,0]
    
#     visited = [[False]*n for _ in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j] and computers[i][j] == 1:
#                 q = deque()
#                 q.append((i,j))

#                 while q:
#                     x, y = q.popleft()
#                     visited[x][y] = True

#                     for dx, dy in zip(dxs, dys):
#                         nx, ny = dx+x, dy+y
#                         if -1<nx<n and -1<ny<n and not visited[nx][ny]:
#                             if computers[nx][ny] == 1:
#                                 q.append((nx,ny))
#                 answer += 1
#     return answer
def solution(n, computers):
    answer = 0

    queue = []
    visited = []

    for a in range(n):
        if a not in visited:
            queue.append(a)
            answer += 1

            while queue :
                now = queue.pop(0)    
                for i in range(n):
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        queue.append(i)
    return answer
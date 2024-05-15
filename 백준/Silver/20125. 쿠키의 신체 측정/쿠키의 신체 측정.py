import sys

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
result = [0,0,0,0,0] # 왼쪽팔, 오른쪽팔, 허리, 왼쪽다리, 오른쪽다리 

# 머리 찾기
heart = [0,0]
flag = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*":
            heart = (i+1, j)
            flag = True
            break
    if flag:
        break

# 왼팔 길이
for i in range(heart[1]-1, -1, -1):
    if graph[heart[0]][i] == "*":
        result[0] += 1
    else: break

# 오른팔 길이
for i in range(heart[1]+1,n):
    if graph[heart[0]][i] == "*":
        result[1] += 1
    else: break

# 허리 길이
wrist = [0,0]
for i in range(heart[0]+1, n):
    if graph[i][heart[1]] == "*":
        result[2] += 1
    else:
        wrist = (i-1, heart[1])
        break

# 왼쪽 다리, 오른쪽 다리
for i in range(wrist[0]+1, n):
    if graph[i][wrist[1]-1] == "*":
        result[3] += 1
    if graph[i][wrist[1]+1] == "*":
        result[4] += 1

print(*list(map(lambda x: x + 1, heart)))      
print(*result)

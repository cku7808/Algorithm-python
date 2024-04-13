import sys

n, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dotproduct(a1, a2):
    result = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a1[i][k]*a2[k][j] % 1000
    return result

def matmul(a,b):
    if b == 1:
        return a
    ans = matmul(a,b//2)
    if b % 2 == 0:
        return dotproduct(ans, ans)
    else:
        return dotproduct(dotproduct(ans, ans), a)
    
answer = matmul(matrix,b)
for i in range(n):
    for j in range(n):
        answer[i][j] %= 1000

for elem in answer:
    print(*elem)

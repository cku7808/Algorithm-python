import sys
n,k = map(int,sys.stdin.readline().split())
arr = []
result = [[0]*(k+1) for _ in range(n+1)]
arr = [(0,0)]
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j-w]+v,result[i-1][j])
print(result[n][k])

import sys
n = int(sys.stdin.readline())

result = [[0]*10 for _ in range(n)]
for i in range(1,10):
    result[0][i] = 1

for i in range(1,n):
    for j in range(10):
        if j==0:
            result[i][j] = result[i-1][j+1]
        elif j==9:
            result[i][j] = result[i-1][j-1]
        else:
            result[i][j] = result[i-1][j-1]+result[i-1][j+1]
print(sum(result[n-1])%1000000000)

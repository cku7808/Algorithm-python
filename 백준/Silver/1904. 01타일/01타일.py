import sys
n = int(sys.stdin.readline())

result = [0]*(n+1)
for i in range(1,n+1):
    if i < 3:
        result[i] = i
    else:
        result[i] = (result[i-1]+result[i-2])%15746
print(result[n])

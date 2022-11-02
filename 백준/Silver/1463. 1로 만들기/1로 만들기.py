import sys
n = int(sys.stdin.readline())

result = [0]*(n+1)

for i in range(2,n+1):
    tmp = []
    if i%3==0:
        tmp.append(result[i//3]+1)
    if i%2==0:
        tmp.append(result[i//2]+1)
    tmp.append(result[i-1]+1)

    result[i] = min(tmp)
print(result[n])


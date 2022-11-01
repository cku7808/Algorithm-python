import sys

n = int(sys.stdin.readline())

cost = [0]*300
for i in range(n):
    cost[i] = int(sys.stdin.readline())

result = [0]*300


result[0] = cost[0]
result[1] = cost[0]+cost[1]
result[2] = max(cost[0],cost[1])+cost[2]
for i in range(3,n):
    result[i] = max(cost[i-1]+result[i-3],result[i-2])+cost[i]

print(result[n-1])

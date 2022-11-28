import sys
n,k = map(int, sys.stdin.readline().split())

coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))


goal = k
cnt = 0
while goal != 0:
    #pointer = 0
    for i in range(n):
        if coin[i] > goal:
            break
        pointer = coin[i]

    while True:
        if goal < pointer:
            break
        cnt += 1
        goal -= pointer

print(cnt)

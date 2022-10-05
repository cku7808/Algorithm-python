import sys
n = int(sys.stdin.readline())

num = 1
cnt = 1
ans = 0
while cnt <= n:
    if "666" in str(num):
        cnt += 1
        ans = num
    num += 1
print(ans)

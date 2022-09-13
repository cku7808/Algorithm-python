n = int(input())
nums = list(map(int,input().split()))

cnt = 0
for elem in nums:
    tmp = 0
    for i in range(2,elem+1):
        if elem % i == 0:
            tmp += 1
    if tmp == 1:
        cnt += 1
print(cnt)

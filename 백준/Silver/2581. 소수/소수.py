m = int(input())
n = int(input())

result = []
for i in range(m,n+1):
    cnt = 0
    for j in range(2,i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 1:
        result.append(i)
if len(result):
    print(sum(result))
    print(min(result))
else:
    print(-1)

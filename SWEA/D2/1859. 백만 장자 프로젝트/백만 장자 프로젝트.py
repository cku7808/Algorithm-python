t = int(input())

for i in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    price.reverse()

    ans = 0
    tmp = 0
    cur_max = price[0]
    for j in range(1,len(price)):
        if cur_max > price[j]:
            tmp += cur_max - price[j]
        else:
            cur_max = price[j]
            ans += tmp
            tmp = 0
    if tmp:
        ans += tmp
    print("#"+str(i),ans)

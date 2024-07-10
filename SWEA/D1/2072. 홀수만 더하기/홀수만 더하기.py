t = int(input())
for i in range(1, t+1):
    ans = 0
    arr = list(map(int, input().split()))
    for n in arr:
        if n%2 != 0:
            ans += n
    print("#"+str(i),ans)
    
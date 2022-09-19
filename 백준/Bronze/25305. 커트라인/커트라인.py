n,k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

for i in range(n-1,n-1-k,-1):
    ans = scores[i]
print(ans)

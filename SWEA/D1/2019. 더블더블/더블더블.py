n = int(input())
ans = []
for i in range(n+1):
    ans.append(pow(2,i))
print(*ans)
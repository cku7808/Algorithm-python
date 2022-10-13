import sys
n,m = map(int,sys.stdin.readline().split())

ans = {}
for _ in range(n+m):
    name = sys.stdin.readline().strip()
    if name in ans:
        ans[name] += 1
    else:
        ans[name] = 1
ans = dict(sorted(ans.items()))
result = []
for k,v in ans.items():
    if v == 2:
        result.append(k)
print(len(result))
for elem in result:
    print(elem)

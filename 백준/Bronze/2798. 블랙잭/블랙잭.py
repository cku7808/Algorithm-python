import sys
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


ans = 0
for i in range(n):
    n1 = arr[i]
    for j in range(i+1,n):
        n2 = arr[j]
        for k in range(j+1,n):
            n3 = arr[k]
            if (n1+n2+n3) <= m and (n1+n2+n3) > ans:
                ans = (n1+n2+n3)
print(ans)

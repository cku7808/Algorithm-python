import sys
a,b = map(int, sys.stdin.readline().split())
arr_a = list(map(int,sys.stdin.readline().split()))
arr_b = list(map(int,sys.stdin.readline().split()))

ans = {}
cnt = 0
for elem in arr_a:
        ans[elem] = 1
for elem in arr_b:
    if elem in ans:
        cnt += 1
print((len(arr_a)-cnt)+(len(arr_b)-cnt))

        

import sys
n,m = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)] #1,2,3,4
check = [False]*n

result = []
ans = []
def dfs(cnt):
    if cnt == m:
        print(*result)
        
        return
    
    for i in range(n):
        if check[i] == True or (len(result)!=0 and max(result)>arr[i]):
            continue
        else:
            result.append(arr[i])
            check[i] = True
            cnt += 1
            dfs(cnt)
            result.pop()
            check[i] = False
            cnt -= 1

dfs(0)

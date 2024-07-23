T = int(input())

def check(arr, x):
    flag = True
    visited = [False]*n
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            if abs(arr[i]-arr[i+1]) != 1:
                flag = False
            elif arr[i+1] > arr[i] :
                target = arr[max(0, i-x+1):i+1]
                if len(target) < x or len(set(target)) != 1 or True in visited[max(0, i-x+1):i+1]:
                    flag = False
                else:
                    visited[max(0, i-x+1):i+1] = [True]*len(target)
                    
            elif arr[i] > arr[i+1]:
                target = arr[i+1:min(n, i+1+x)]
                if len(target) < x or len(set(target)) != 1 or True in visited[i+1:min(n, i+1+x)]:
                    flag = False
                else:
                    visited[i+1:min(n, i+1+x)] = [True]*len(target)
    return flag

for i in range(1, T+1):
    n, x = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        result1 = check(grid[j], x)
        if result1:
            cnt += 1
    
    for elem in zip(*grid):
        result2 = check(elem, x)
        if result2:
            cnt += 1
    print(f"#{i} {cnt}")
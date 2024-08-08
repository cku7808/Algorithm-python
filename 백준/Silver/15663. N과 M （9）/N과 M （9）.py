import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
final_arr = []
tmp_arr = []
visited = [False]*n

def backtrack(tmp_arr, cnt):
    global final_arr
    if cnt == m:
        final_arr.append(tuple(tmp_arr))
        return
    for i in range(n):
        if not visited[i]:
            tmp_arr.append(arr[i])
            visited[i] = True
            backtrack(tmp_arr, cnt+1)
            tmp_arr.pop()
            visited[i] = False

backtrack(tmp_arr, 0)
final_arr = list(set(final_arr))
final_arr.sort()

for elem in final_arr:
    print(*elem)
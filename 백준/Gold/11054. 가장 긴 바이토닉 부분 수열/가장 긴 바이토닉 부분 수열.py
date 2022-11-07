import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(reversed(arr[:]))

def cal(arr):
    result = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                result[i] = max(result[i], result[j]+1)
    return result


arr = cal(arr)
#print(arr)
arr2 = list(reversed(cal(arr2)))
#print(arr2)

ans = 0
for a, b in zip(arr, arr2):
    if ans < (a+b)-1:
        ans = a+b-1

print(ans)


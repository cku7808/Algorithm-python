import sys
a, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = []

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr)+1)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    ans = []
    i,j = 0,0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            ans.append(left[i])
            result.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            result.append(right[j])
            j+=1
    while len(left) > i:
        ans.append(left[i])
        result.append(left[i])
        i+=1
    while len(right) > j:
        ans.append(right[j])
        result.append(right[j])
        j+=1
    return ans

merge_sort(arr)
if len(result) < k:
    print(-1)
else:
    print(result[k-1])

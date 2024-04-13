import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

arr.sort()

for elem in target:
    left, right = 0, n-1
    flag = False
    
    while left <= right:
        mid = (left+right)//2

        if arr[mid] == elem:
            flag = True
            break
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
            
    if flag:
        print(1)
    else:
        print(0)
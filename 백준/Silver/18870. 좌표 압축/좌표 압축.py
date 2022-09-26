import sys
n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))

tmp2 = set(tmp[:])
tmp2 = list(tmp2)
tmp2.sort()

def BinarySearch(num,arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if num == arr[mid]:
            return mid
        elif arr[mid] > num:
            end = mid-1
        else:
            start = mid+1
    


for elem in tmp:
    print(BinarySearch(elem,tmp2), end=" ")

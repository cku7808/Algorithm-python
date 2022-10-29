import sys
t = int(sys.stdin.readline())

arr = [0]*(101)

arr[1], arr[2], arr[3] = 1,1,1
arr[4], arr[5] = 2,2
for i in range(6,101):
    arr[i] = arr[i-5] + arr[i-1]

for _ in range(t):
    print(arr[int(sys.stdin.readline())])
    

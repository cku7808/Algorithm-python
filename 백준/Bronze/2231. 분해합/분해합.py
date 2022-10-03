import sys
n = int(sys.stdin.readline())

min_ans = sys.maxsize
for i in range(1,n+1):
    Sum = i
    for elem in str(i):
        Sum += int(elem)

    if Sum == n and min_ans > i:
        min_ans = i
if min_ans == sys.maxsize:
    print(0)
else:
    print(min_ans)
        

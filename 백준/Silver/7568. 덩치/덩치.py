import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))
ans = [0]*len(arr)

for i in range(len(arr)):
    x,y = arr[i][0], arr[i][1]
    num = 1
    for j in range(len(arr)):
        a, b = arr[j][0], arr[j][1]
        if a == x and b == y:
            continue
        else:
            if a>x and b>y:
                num += 1
    ans[i] = str(num)
print(" ".join(ans))


import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    arr.append((len(tmp),tmp))
arr = list(set(arr))


arr.sort(key=lambda x: (x[0],x[1]))

for elem in arr:
    print(elem[1])

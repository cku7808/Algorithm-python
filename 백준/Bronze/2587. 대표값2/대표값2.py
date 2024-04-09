import sys

s = 0
arr = []
for _ in range(5):
    num = int(sys.stdin.readline())
    s += num
    arr.append(num)
arr.sort()
print(s//5)
print(arr[2])
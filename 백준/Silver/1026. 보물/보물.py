import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()

answer = 0
for i, j in zip(a,b):
    answer += i*j
print(answer)

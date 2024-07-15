import sys

n = int(sys.stdin.readline())

x = []
y = []

if n > 1:
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()

    print((x[-1]-x[0])*(y[-1]-y[0]))
else:
    print(0)

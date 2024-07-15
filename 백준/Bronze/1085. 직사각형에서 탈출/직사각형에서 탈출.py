import sys, math

x, y, w, h = map(int, sys.stdin.readline().split())

dist1 = min(x, y)
dist2 = min(abs(x-w), abs(y-h))

print(dist1 if dist1 < dist2 else dist2)

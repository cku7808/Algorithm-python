import sys, math

h, w, n, m = map(int, sys.stdin.readline().split())

row = math.ceil(w / (m+1))
col = math.ceil(h / (n+1))

print(row*col)
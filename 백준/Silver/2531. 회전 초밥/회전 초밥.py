import sys

n, d, k, c = map(int, sys.stdin.readline().split())

sushi = [int(sys.stdin.readline()) for _ in range(n)]*2

max_cnt = 0
for i in range(n):
    window = set(sushi[i:i+k])
    window.add(c)
    max_cnt = max(max_cnt, len(window))
print(max_cnt)
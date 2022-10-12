import sys

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

hashing = {}
for elem in card:
    if elem in hashing:
        hashing[elem] += 1
    else:
        hashing[elem] = 1

ans = []
for elem in check:
    if elem in hashing:
        ans.append(str(hashing[elem]))
    else:
        ans.append("0")
print(" ".join(ans))

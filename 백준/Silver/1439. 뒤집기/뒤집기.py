import sys

s = sys.stdin.readline().strip()
zero_num = 0
one_num = 0
cur = -1
for elem in s:
    if elem != cur:
        cur = elem
        if elem == "0":
            zero_num += 1
        else:
            one_num += 1
print(min(zero_num, one_num))

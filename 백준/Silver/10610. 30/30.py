import sys

n = sys.stdin.readline().strip()

if "0" not in set(list(n)):
    print(-1)
else:
    arr = sorted(list(n),reverse=True)
    sum_n = sum(map(int,list(n)))
    if sum_n%3 == 0:
        print("".join(arr))
    else:
        print(-1)

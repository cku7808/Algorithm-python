import sys

t = int(sys.stdin.readline())

for _ in range(t):
    day = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.reverse()

    max_val = arr[0]
    benefit = 0
    for elem in arr[1:]:
        if max_val > elem:
            benefit += max_val-elem
        else:
            max_val = elem
    print(benefit)

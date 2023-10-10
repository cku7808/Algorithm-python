import sys

p = int(sys.stdin.readline())

for _ in range(p):
    tmp = sys.stdin.readline().split()
    t = tmp[0]
    lst = list(map(int, tmp[1:]))

    ans = 0
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                ans += 1
    print(t, ans)

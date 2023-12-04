import sys

t = int(sys.stdin.readline())

for _ in range(t):
    w = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    ans1 = sys.maxsize
    ans2 = 0

    char_dict = {}
    for idx, c in enumerate(w):
        if c not in char_dict:
            char_dict[c] = [idx]
        else:
            char_dict[c].append(idx)

    for key, val in char_dict.items():
        if len(val) >= k:
            for j in range(len(val)-k+1):
                length = val[j+k-1] - val[j] + 1
                ans1 = min(length, ans1)
                ans2 = max(length, ans2)
                
    if ans1 == sys.maxsize or ans2 == 0:
        print(-1)
    else:
        print(ans1, ans2)
import sys, heapq

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    tnum = list(map(int, sys.stdin.readline().split()))
    score = 1
    check = dict()
    for i in range(n):
        if tnum.count(tnum[i]) < 6:
            continue
        else:
            try:
                check[str(tnum[i])].append(score)
            except:
                check[str(tnum[i])] = []
                check[str(tnum[i])].append(score)
            finally:
                score += 1
    result = []
    for k, v in check.items():
        result.append((sum(v[:4]),v[4],k))

    heapq.heapify(result)
    ans = heapq.heappop(result)
    print(ans[-1])

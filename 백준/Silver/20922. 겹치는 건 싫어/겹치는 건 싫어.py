import sys

n, k = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().split())

cnt = dict()

left, right = 0, 0
max_cnt = 0
while right < n:
    if a[right] not in cnt:
        cnt[a[right]] = 0
        
    if cnt[a[right]] != k:
        cnt[a[right]] += 1
        right += 1
        
    else:
        cnt[a[left]] -= 1
        left += 1

    max_cnt = max(max_cnt, right-left)
print(max_cnt)

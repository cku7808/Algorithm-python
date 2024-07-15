import sys

arr = []
max_len = 0
for _ in range(5):
    s = sys.stdin.readline().strip()
    arr.append(s)
    max_len = max(max_len,len(s))

ans = ""
for i in range(max_len):
    for j in range(5):
        try:
            ans += arr[j][i]
        except:
            continue
print(ans)

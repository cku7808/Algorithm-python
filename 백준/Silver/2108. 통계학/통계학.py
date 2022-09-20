import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

avr = round(sum(arr)/n)
ran = max(arr) - min(arr)

arr.sort() 
mid = arr[n//2]

tmp = Counter(arr).most_common()
if len(tmp) == 1:
    mode = tmp[0][0]
else:
    if tmp[0][1] > tmp[1][1]:
        mode = tmp[0][0]
    elif tmp[0][1] == tmp[1][1]:
        mode = tmp[1][0]


print(avr)
print(mid)
print(mode)
print(ran)

import sys

s = int(sys.stdin.readline())

cnt = 0
sum_num = 0
i = 1
while True:
    if sum_num < s:
        cnt += 1
        sum_num += i
        i += 1
    else:
        if sum_num == s:
            print(cnt)
        else:
            print(cnt - 1)
        break

from collections import deque
K = int(input())
lst = [[] for _ in range(5)]
d_count = [0 for _ in range(5)]
input_lst = deque()
for _ in range(6):
    d, l = map(int, input().split())
    lst[d].append(l)
    d_count[d] += 1
    input_lst.append((d, l))

re_lst = []
blank = []
while input_lst:
    tmp = input_lst.popleft()
    if d_count[tmp[0]] == 1:
        re_lst.append(tmp)
    else:
        if len(re_lst) < 2:
            input_lst.append(tmp)
        else:
            blank.append(tmp)

area = re_lst[0][1] * re_lst[1][1]
blank_area = blank[1][1] * blank[2][1]
answer = area - blank_area
print(answer*K)
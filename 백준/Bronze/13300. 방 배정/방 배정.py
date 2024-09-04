N, K = map(int, input().split())
y_1 = [[] for _ in range(2)]
y_2 = [[] for _ in range(2)]
y_3 = [[] for _ in range(2)]
y_4 = [[] for _ in range(2)]
y_5 = [[] for _ in range(2)]
y_6 = [[] for _ in range(2)]
person = 1
for _ in range(N):
    # S = 성별, Y = 학년
    S, Y = map(int, input().split())
    if Y == 1:
        y_1[S].append(person)
    elif Y == 2:
        y_2[S].append(person)
    elif Y == 3:
        y_3[S].append(person)
    elif Y == 4:
        y_4[S].append(person)
    elif Y == 5:
        y_5[S].append(person)
    else:
        y_6[S].append(person)

room_cnt = 0
for lst in [y_1, y_2, y_3, y_4, y_5, y_6]:
    for s_lst in lst:
        if len(s_lst) % K > 0:
            room_cnt += len(s_lst)//K + 1
        else:
            room_cnt += len(s_lst)//K
print(room_cnt)
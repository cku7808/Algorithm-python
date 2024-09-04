graph = [[0]*1001 for _ in range(1001)]
N = int(input())
idx = 1
for _ in range(N):

    start_x, start_y, width, height = map(int, input().split())
    for i in range(start_x, start_x+width):
        for j in range(start_y, start_y+height):
            graph[i][j] = idx
    idx += 1
cnt_lst = dict()

for n in range(1, 1 + N):
    cnt = 0
    for idx in range(1001):
        for jdx in range(1001):

            if graph[idx][jdx] == n:
                cnt += 1
    cnt_lst[n] = cnt

for ans in cnt_lst.keys():
    print(cnt_lst[ans])
n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    score = arr[1:]
    avr = sum(score)/arr[0]
    cnt = 0
    for elem in score:
        if elem > avr:
            cnt += 1
    print('%.3f' %(cnt/arr[0]*100), end='')
    print('%')

A, B, C, M = map(int, input().split())
time = 0
tired = 0
work = 0
while True:
    if time == 24:
        break


    if tired <= (M - A):
        tired += A
        work += B
        time += 1

    elif tired > (M - A):
        tired -= C
        time += 1

        if tired < 0:
            tired = 0

print(work)
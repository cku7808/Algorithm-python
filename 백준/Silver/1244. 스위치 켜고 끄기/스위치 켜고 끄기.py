def man(num):

    for idx in range(N):
        if idx+1 > N:
            break
        if (idx+1) % num == 0:
            switch[idx] = 1-switch[idx]

def woman(num):

    jdx = num - 1
    if switch[jdx]:
        switch[jdx] = 0
    else:
        switch[jdx] = 1
    l = jdx-1
    r = jdx+1
    if l < 0 or r > N-1:
        return

    if switch[l] == switch[r]:
        while True:
            switch[l] = 1-switch[l]
            switch[r] = 1-switch[r]
            l -= 1
            r += 1
            if l < 0 or r == N or switch[l] != switch[r]:
                break
    else:
        return

N = int(input())
switch = list(map(int, input().split()))
n = int(input())

for _ in range(n):

    s, num = map(int, input().split())
    # 남자일 때
    if s == 1:
        man(num)

    elif s == 2:
        woman(num)

n = 20
for w in range(0, N+n, n):
    print(*switch[w:w+n])
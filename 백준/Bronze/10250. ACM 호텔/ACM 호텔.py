t = int(input())

for _ in range(t):
    h,w,n = map(int, input().split())
    floor = n%h
    rnum = n//h+1
    if floor == 0:
        floor = h
        rnum = n//h

    result = str(floor)+str(rnum).zfill(2)
    print(result)
    

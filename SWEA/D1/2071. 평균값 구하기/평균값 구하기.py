t = int(input())
for i in range(1, t+1):
    avg = round(sum(map(int, input().split())) / 10)
    print("#"+str(i), avg)
    
t = int(input())

for i in range(1, 1+t):
    ans = -1
    s = input()
    year = s[:4]
    month = s[4:6]
    day = s[6:]
    if 0<int(month)<13 and 0<int(day)<32:
        if int(month) == 2 and int(day) <= 28:
            ans = year+"/"+month+"/"+day
        elif int(month) in [4,6,9,11] and int(day) <= 30:
            ans = year+"/"+month+"/"+day
        elif int(month) in [1,3,5,7,8,10,12] and int(day) <= 31:
            ans = year+"/"+month+"/"+day   
    print("#"+str(i),end=" ")
    print(ans)
n = int(input())

def find(n):
    cnt = 0
    for i in range(1,n+1):
        if i < 100:
            cnt += 1
        else:
            s = str(i)
            ans = True
            d = int(s[1]) - int(s[0])
            for j in range(1,len(s)-1):
                if int(s[j+1]) - int(s[j]) != d:
                    ans = False
                    break
            if ans:
                cnt += 1
    return cnt

print(find(n))

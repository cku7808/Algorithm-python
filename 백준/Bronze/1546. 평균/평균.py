n = int(input())
s = list(map(int, input().split()))

max_num = max(s)
for i in range(n):
    s[i] = s[i]/max_num*100
    
print(sum(s)/n)
import sys
import re
s = sys.stdin.readline().strip()

tmp = ""
arr = []
for i in range(len(s)):
    if s[i] not in "+-":
        tmp += s[i]
    else:
        arr.append(int(tmp))
        arr.append(s[i])
        tmp = ""
arr.append(int(tmp))

check = [False]*len(arr)
ans = arr[0]
check[0] = True

for i in range(1,len(arr)):
    if check[i] == True:
        continue
    if arr[i] == "-":
        check[i] = True
        for j in range(i+1,len(arr)):
            if arr[j] == "-":
                break
            if type(arr[j]) == int :
                ans -= arr[j]
                check[j] = True
            else:
                check[j] = True
    elif arr[i] == "+":
        check[i] = True
    else:
        ans += arr[i]

print(ans)    





            
        

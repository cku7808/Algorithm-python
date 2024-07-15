import sys

n, b = sys.stdin.readline().split()
b = int(b)

ans = 0

try:
    target = int(n)
except:
    for i, elem in enumerate(n[::-1]):
        try:
            int(elem)
        except:
            ans += (b**i)*(ord(elem)-55)
        else:
            ans += (b**i)*int(elem)
else:
    for i, elem in enumerate(n[::-1]):
        ans += (b**i)*int(elem)      
    
print(ans)

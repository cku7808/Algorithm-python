w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# t시간 후 개미좌표

a, b = p+t, q+t

x, y = a % (w*2), b % (h*2)

if x <= w and y <= h:
    print(x, y)
elif x <= w and y > h:
    print(x, 2*h - y)
elif x > w and y <= h:
    print(2*w - x, y)
else:
    print(2*w - x, 2*h - y)
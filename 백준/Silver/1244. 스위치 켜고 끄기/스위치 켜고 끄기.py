import sys
# abs(num-1)

n = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
switches.insert(0,0)
num_students = int(sys.stdin.readline())

def male(num):
    for i in range(num, n+1, num):
        switches[i] = abs(switches[i]-1)
        
def female(num):
    switches[num] = abs(switches[num]-1)
    for i in range(1,n//2):
        left, right = num-i, num+i
        if left >= 1 and right <= n:
            if switches[left] == switches[right]:
                switches[left] = abs(switches[left]-1)
                switches[right] = abs(switches[right]-1)
            else:
                break
            

for _ in range(num_students):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        male(num)
    else:
        female(num)

result = switches[1:]

for i in range(0, n, 20):
    print(*result[i:i+20])

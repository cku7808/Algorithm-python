arr = [0]*10001

def make_list(arr):
    for i in range(1,10001):
        ans = i
        for j in str(i):
            ans += int(j)
        if ans <= 10000:
            arr[ans] += 1
        
make_list(arr)
for i in range(1,len(arr)):
    if arr[i] == 0:
        print(i)

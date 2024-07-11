
t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    nums = list(input().strip())

    result = set()
    for j in range(n//4):
        for z in range(0,n,n//4):
            result.add("".join(nums[z:z+n//4]))
    
        nums.insert(0,nums.pop())
    result = sorted(list(map(lambda x : int(x,16), result)), reverse=True)

    print("#"+str(i),result[k-1])

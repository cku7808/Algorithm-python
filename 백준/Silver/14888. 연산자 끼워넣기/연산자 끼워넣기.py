import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_ans = sys.maxsize*(-1)
min_ans = sys.maxsize
op_arr = []

def cal(op_arr, arr):
    arr_pointer = 1
    op_pointer = 0
    result = arr[0]
    op_cur = -1

    while arr_pointer <= len(arr)-1 or op_pointer <= len(op_arr)-1:
        op_cur = op_arr[op_pointer]
        tmp = arr[arr_pointer]

        if op_cur == 0:
            result += tmp
        elif op_cur == 1:
            result -= tmp
        elif op_cur == 2:
            result *= tmp
        else:
            if result < 0:
                result *= -1
                result //= tmp
                result *= -1
            else:
                result //= tmp
        op_pointer += 1
        arr_pointer += 1
        
    return result

def sol(cnt):
    global max_ans, min_ans
    if cnt == n-1:
        ans = cal(op_arr, arr)
        if max_ans < ans:
            max_ans = ans
        if min_ans > ans:
            min_ans = ans
        return
    else:
        for i in range(4):
            if op[i] != 0:
                op_arr.append(i)
                op[i] -= 1
                sol(cnt+1)
                op[i] += 1
                op_arr.pop()
                
sol(0)    
print(max_ans)
print(min_ans)

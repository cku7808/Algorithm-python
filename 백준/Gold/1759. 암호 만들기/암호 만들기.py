import sys

l,c = map(int, sys.stdin.readline().split())
s = sorted(sys.stdin.readline().split())

alpha = {
    "a":1,
    "e":1,
    "i":1,
    "o":1,
    "u":1}

def check(stack):
    cons_num = 0
    vow_num = 0
    for elem in stack:
        if elem in alpha.keys():
            vow_num += 1
        else:
            cons_num += 1
    return vow_num, cons_num

def solution(stack, idx):
    if len(stack) == l:
        vow_num, cons_num = check(stack)
        if vow_num >= 1 and cons_num >= 2:
            print("".join(stack))
            return

    for i in range(idx, c):
        stack.append(s[i])
        solution(stack, i+1)
        stack.pop()

solution([], 0)
    

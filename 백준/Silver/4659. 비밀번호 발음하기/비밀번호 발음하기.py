import sys

while True:
    s = sys.stdin.readline().strip()
    if s == "end":
        break

    flag = True
    
    if len(set(list("aeiou")).intersection(set(list(s)))) == 0:
        flag = False

    arr = []
    for i in s:
        if i in "aeiou":
            arr.append("모음")
        else:
            arr.append("자음")
    
    for i in range(1,len(s)-1):
        if arr[i-1] == arr[i] == arr[i+1]:
            flag = False
            break
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] != "e" and s[i] != "o":
                flag = False
                break
    if flag:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")

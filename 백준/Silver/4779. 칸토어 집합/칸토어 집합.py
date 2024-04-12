import sys

def remove_line(s):
    if len(s) <= 1:
        return "-"
        
    start = len(s)//3
    end = start*2

    s1 = s[:start]
    s2 = s[end:]

    return remove_line(s1)+" "*start+remove_line(s2)

while True:
    try:
        n = int(sys.stdin.readline())

        s = "-"*3**n
        s = remove_line(s)
        print(s)
    except:
        break
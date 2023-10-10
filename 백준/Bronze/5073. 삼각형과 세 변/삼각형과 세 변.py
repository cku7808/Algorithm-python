import sys

while True:
    s = sys.stdin.readline()
    if s == "0 0 0\n":
        break
    o, tw, th = map(int, s.split())
    
    max_num = max(o, tw, th)
    other = o + th + tw - max_num
    
    if other <= max_num :
        print("Invalid")
    elif o == tw and o == th and tw == th:
        print("Equilateral")
    elif o != tw and o != th and tw != th:
        print("Scalene")
    else:
        print("Isosceles")
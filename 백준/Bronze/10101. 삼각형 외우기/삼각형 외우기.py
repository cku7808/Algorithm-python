import sys

angles = set()
sums = 0

for _ in range(3):
    angle = int(sys.stdin.readline())
    sums += angle
    angles.add(angle)

if sums != 180:
    print("Error")
else:
    if len(angles) <= 1:
        print("Equilateral")
    elif len(angles) < 3:
        print("Isosceles")
    else:
        print("Scalene")

import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().strip()

def move_balls(ball,s):
    s=s.lstrip(ball)
    return s.count(ball)

print(min(
    move_balls("R",arr),
    move_balls("R",arr[::-1]),
    move_balls("B",arr),
    move_balls("B",arr[::-1])))
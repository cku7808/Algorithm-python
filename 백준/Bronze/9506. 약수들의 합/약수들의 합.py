import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    
    num = 0
    string = []
    for i in range(1, n):
        if n%i == 0:
            num += i
            string.append(str(i))

    if num == n:
        print(n,"="," + ".join(string))
    else:
        print(n, "is NOT perfect.")

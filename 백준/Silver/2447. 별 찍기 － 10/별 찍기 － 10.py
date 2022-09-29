import sys
n = int(sys.stdin.readline())

def star(n):
    if n == 1:
        return ["*"]

    Star = star(n//3)

    ans = []

    for elem in Star:
        ans.append(elem*3)
    for elem in Star:
        ans.append(elem+" "*(n//3)+elem)
    for elem in Star:
        ans.append(elem*3)


    return ans

print("\n".join(star(n)))


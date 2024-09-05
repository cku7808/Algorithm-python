N = int(input())
for _ in range(N):
    A_input = list(map(int, input().split()))
    B_input = list(map(int, input().split()))
    A_n = A_input[0]
    B_n = B_input[0]
    A = A_input[1:]
    B = B_input[1:]
    A = sorted(A)
    B = sorted(B)
    A_count = (A.count(4), A.count(3), A.count(2), A.count(1))
    B_count = (B.count(4), B.count(3), B.count(2), B.count(1))
    if A_count == B_count:
        print('D')
    elif A_count == max(A_count, B_count):
        print('A')
    else:
        print('B')
def solution(brown, yellow):
    arr = []
    tmp = brown+yellow
    for i in range(1,tmp):
        if tmp%i == 0:
            a = i
            b = tmp//i
            if a>=b:
                if 2*a+2*b-4 == brown:
                    return [a,b]
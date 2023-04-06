import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    # 진법 변환
    tmp = ""
    while n>0:
        tmp += str(n%k)
        n = n//k
    tmp = tmp[::-1].split("0")

    # 0기준 스플릿, 정수 변환, 소수 판별
    # result = [int(elem) for elem in tmp.split("0") if elem != "" and int(elem)>1]
    for elem in tmp:
        if elem != "" and int(elem)>1:
            if is_prime_number(int(elem)):
                answer += 1
    
    return answer
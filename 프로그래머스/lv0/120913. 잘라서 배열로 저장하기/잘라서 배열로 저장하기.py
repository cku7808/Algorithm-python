def solution(my_str, n):
    answer = []
    length = len(my_str)//n
    for _ in range(length):
        answer.append(my_str[:n])
        my_str = my_str[n:]
    if my_str != "":
        answer.append(my_str)
    return answer
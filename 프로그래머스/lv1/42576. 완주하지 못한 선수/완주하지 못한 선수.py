def solution(participant, completion):
    answer = ""
    check_dict = {}
    for name in participant:
        if name not in check_dict.keys():
            check_dict[name] = 1
        else:
            check_dict[name] += 1
    for name in completion:
        if name in check_dict.keys():
            check_dict[name] -= 1
    
    for name, cnt in check_dict.items():
        if cnt > 0:
            answer = name
    return answer
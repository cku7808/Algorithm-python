def solution(clothes):
    cloth_dict = {}
    answer = 1
    
    for name, c_type in clothes:
        if c_type not in cloth_dict.keys():
            cloth_dict[c_type] = ["X",name]
        else:
            cloth_dict[c_type].append(name)
    
    for val in cloth_dict.values():
        answer *= len(val)
    answer -= 1
    return answer
        

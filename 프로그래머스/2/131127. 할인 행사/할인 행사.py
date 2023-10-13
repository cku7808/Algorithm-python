def check(want_dict, checklist):
    if len(set(checklist)) != len(want_dict) or set(checklist) != set(want_dict.keys()):
        return False
    else:
        tmp_dict = {}
        for elem in checklist:
            if elem not in tmp_dict:
                tmp_dict[elem] = 1
            else:
                tmp_dict[elem] += 1
        for elem in set(checklist):
            if want_dict[elem] != tmp_dict[elem]:
                return False
        return True

def solution(want, number, discount):
    want_dict = {}
    for w,n in zip(want, number):
        want_dict[w] = n
    
    ans = 0
    for i in range(len(discount)-len(want)+1):
        checklist = discount[i:i+sum(number)]
        if check(want_dict, checklist):
            ans += 1
    return ans
        
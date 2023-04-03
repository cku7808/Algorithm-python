def cal_dist(a,b):
    x,y = a
    n,m = b
    return abs(x-n)+abs(y-m)

def solution(numbers, hand):
    answer = ''
    left_h = (3,0)
    right_h = (3,2)
    
    key_dict = {"1":(0,0),"2":(0,1),"3":(0,2),
               "4":(1,0), "5":(1,1),"6":(1,2),
               "7":(2,0), "8":(2,1),"9":(2,2),
               "0":(3,1)}
    
    for elem in numbers:
        elem = str(elem)
        if elem in "147":
            answer += "L"
            left_h = key_dict[elem]
        elif elem in "369":
            answer += "R"
            right_h = key_dict[elem]
        else:
            dist_l = cal_dist(key_dict[elem], left_h)
            dist_r = cal_dist(key_dict[elem], right_h)
            if dist_l>dist_r:
                answer += "R"
                right_h = key_dict[elem]
            elif dist_l<dist_r:
                answer += "L"
                left_h = key_dict[elem]
            else:
                if hand == "left":
                    answer += "L"
                    left_h = key_dict[elem]
                else:
                    answer += "R"
                    right_h = key_dict[elem]

    return answer
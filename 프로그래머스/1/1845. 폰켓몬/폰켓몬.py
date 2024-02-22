def solution(nums):
    target_num = len(nums)/2
    unique_num = len(set(nums))
    
    if target_num > unique_num : 
        return unique_num
    else:
        return target_num

    
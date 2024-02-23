def solution(s):
    stack = []
    
    for elem in s:
        if elem == "(":
            stack.append(elem)
        else:
            if not len(stack):
                return False
            stack.pop()
    return not stack
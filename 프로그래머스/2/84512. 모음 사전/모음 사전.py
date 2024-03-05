from itertools import product

def solution(word):
    word_dict = []
    for i in range(1,6):
        for elem in product(['A','E','I','O','U'], repeat=i):
            word_dict.append("".join(elem))
    word_dict.sort()
    return word_dict.index(word)+1
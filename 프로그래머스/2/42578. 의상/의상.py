from collections import Counter
from functools import reduce
def solution(clothes):
    dict_cnt = Counter([x[1] for x in clothes])
    answ = reduce(lambda x, y: x*(y+1), dict_cnt.values(), 1) - 1
    
    return answ
        
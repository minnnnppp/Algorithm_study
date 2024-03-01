from collections import Counter
from functools import reduce
def solution(clothes):
    # 1) 종류별 가짓수 집계
    _dict = Counter([kind for name, kind in clothes])
    # 2) 총 조합수 집계
    answ = reduce(lambda x, y: x*(y+1), _dict.values(), 1) - 1
    
    return answ
    
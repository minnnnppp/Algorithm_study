from functools import reduce
def solution(clothes):
    answ = 1
    dict_cnt = {x[1]:0 for x in clothes}
    for i in clothes:
        dict_cnt[i[1]]+=1
    
    for v in dict_cnt.values():
        answ*=(v+1)
    
    return answ-1
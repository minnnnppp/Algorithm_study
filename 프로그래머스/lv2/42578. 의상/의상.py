def solution(clothes):
    dict_clothes = {_lst[-1]:[] for _lst in clothes}
    for _lst in clothes:
        dict_clothes[_lst[-1]].append(_lst[0])
    
    cnt = 1
    for _v in dict_clothes.values():
        cnt*=(len(_v)+1)
    
    return cnt-1
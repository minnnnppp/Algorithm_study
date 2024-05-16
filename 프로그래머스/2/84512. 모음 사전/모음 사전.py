from itertools import product
def solution(word):
    cnt = 1
    lst_answ = list(word)
    lst_w = ['A', 'E', 'I', 'O', 'U']
    lst_new = []
    
    for i in range(1, 6):
        for comb in product(lst_w, repeat = i):
            lst_new.append(list(comb))
    
    lst_new.sort()
    
    for w in lst_new:
        if w == lst_answ:
            return cnt
        else:
            cnt+=1
    
    
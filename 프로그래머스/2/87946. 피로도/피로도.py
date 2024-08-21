from itertools import permutations
def solution(k, dungeons):
    lst_combs = list(permutations(dungeons, len(dungeons)))
    answ = []
    
    for c in lst_combs:
        target, cnt = k, 0
        for d in c:
            x, y = d[0], d[-1]
            if target >= x:
                cnt +=1
                target -= y
            else:
                pass
        answ.append(cnt)

    return max(answ)
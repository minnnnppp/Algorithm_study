from collections import Counter
def solution(participant, completion):
    cnt = Counter(participant)
    for p in completion:
        if cnt[p] > 0:
            cnt[p] -=1
            
    answ = [x for x in cnt.keys() if cnt[x]>0]
    
    return answ[0]
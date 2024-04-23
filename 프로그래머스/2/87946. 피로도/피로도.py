from itertools import permutations
def solution(k, dungeons):
    lst_permutations = list(permutations(dungeons, len(dungeons)))
    lst_k = []
    for dg in lst_permutations:
        remain, cnt = k, 0
        for d in dg:
            if remain >= d[0] :
                remain-=d[1]
                cnt+=1
            else: 
                break
        lst_k.append(cnt)
        
    return max(lst_k)
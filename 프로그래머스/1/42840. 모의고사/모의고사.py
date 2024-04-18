def solution(answers):
    type1 = [1, 2, 3, 4, 5]
    type2 = [2, 1, 2, 3, 2, 4, 2, 5]
    type3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    dict_cnt = {x:0 for x in range(1,4)}
    
    for i, a in list(enumerate(answers)):
        if a==type1[i%len(type1)]:
            dict_cnt[1]+=1
        if a==type2[i%len(type2)]:
            dict_cnt[2]+=1
        if a==type3[i%len(type3)]:
            dict_cnt[3]+=1
            
    
    max_v = max(dict_cnt.values())
    return [x for x in dict_cnt.keys() if dict_cnt[x]==max_v]
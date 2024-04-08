import operator
def solution(genres, plays):
    answ = []
    plays = list(enumerate(plays))
    _dict = {}
    _dict_sum = {}
    for g, p in zip(genres, plays):
        if g in _dict.keys():
            _dict[g].append(p)
            _dict_sum[g] += p[1]
        else:
            _dict[g] = [p]
            _dict_sum[g] = p[1]
    lst_rev_g = [
        x[0] for x in sorted(
            _dict_sum.items(), key=operator.itemgetter(1), reverse=True
        )]
    
    for g in lst_rev_g:
        _target = sorted(_dict[g], key = lambda x: x[1], reverse=True)
        answ.extend([x[0] for x in _target[:2]])
        
    return answ
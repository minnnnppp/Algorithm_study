def solution(genres, plays):
    _genres_total = {}
    _plays = sorted(list(enumerate(plays)), key = lambda x: x[1], reverse = True)
    _genres = list(enumerate(genres))
    _plays_idx = {}
    answ = []
    
    for g, p in zip(genres, plays):
        if g in _genres_total:
            _genres_total[g].append(p)
        else:
            _genres_total[g] = [p]

    # 2) 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    for p in _plays:
        _g = [x[1] for x in _genres if x[0]==p[0]][0]
        if _g in _plays_idx.keys():
            _plays_idx[_g].append(p[0])
        else:
            _plays_idx[_g] = [p[0]]

    _plays_idx

    # 3) 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    for x in sorted(_genres_total.items(), key=lambda x : sum(x[1]), reverse=True):
        _g = x[0]
        answ += _plays_idx[_g][:2]
    
    return answ
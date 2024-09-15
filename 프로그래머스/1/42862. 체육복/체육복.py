def solution(n, lost, reserve):
    total = [i for i in range(1, n+1)]
    _reserve = sorted(list(set(reserve) - set(lost)))
    _lost = sorted(list(set(lost) - set(reserve)))
    # _reserve_c = _reserve.copy()
    _lost_c = _lost.copy()
    
    for l in _lost:
        lst_targets = [r for r in _reserve if l == r or l == r-1 or l == r+1]
        if lst_targets:
            y = min(lst_targets)
            _lost_c.remove(l)
            _reserve.remove(y)
            
    return n-len(_lost_c)
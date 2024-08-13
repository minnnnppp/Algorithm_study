def solution(sizes):
    maxx, minn = 0, 0
    for s in sizes:
        _max = max(s[0], s[-1])
        _min = min(s[0], s[-1])
        
        if maxx== 0 and minn == 0:
            maxx = _max
            minn = _min
        else:
            maxx = max(maxx, _max)
            minn = max(minn, _min)
    
    return maxx*minn
        
        
            
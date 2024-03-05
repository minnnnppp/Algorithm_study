def solution(n, times):
    _l = min(times)
    _r = max(times)*n
    
    while _l <= _r:
        _m = (_r+_l)//2
        cnt = 0
        for t in times:
            cnt += _m//t
            if cnt >= n: break
            
        if cnt >= n: 
            answ = _m
            _r = _m-1
        elif cnt < n:
            _l = _m+1
            
    return answ
        
            
            
            
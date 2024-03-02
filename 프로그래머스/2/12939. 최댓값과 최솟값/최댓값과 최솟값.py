def solution(s):
    _sp = s.split(' ')
    _lst = [int(x) for x in _sp]
    _max = max(_lst)
    _min = min(_lst)
    
    return ' '.join(map(str, sorted([_max, _min])))
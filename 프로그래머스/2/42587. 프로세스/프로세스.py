def solution(priorities, location):
    answ = 0
    _lst = list(enumerate(priorities))
    while True:
        _s = _lst.pop(0)
        if any(_s[1] < x[1] for x in _lst):
            _lst.append(_s)
        else:
            answ += 1
            if location == _s[0]:
                return answ
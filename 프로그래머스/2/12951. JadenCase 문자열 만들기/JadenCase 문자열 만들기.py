def solution(s):
    # _sentence = list(enumerate(s.split(' ')))
    _sentence = s.split(' ')
    _answ = ''
    for _w in _sentence:
        _answ += _w.capitalize() + ' '
            
    return _answ[:-1]
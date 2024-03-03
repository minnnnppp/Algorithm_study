def solution(n):
    # 1) 피보나치 수열 값 구하기
    _lst_v = [0, 1]
    for i in range(2, n+1):
        _value = _lst_v[i-2]+_lst_v[i-1]
        _lst_v.append(_value)
    # 2) 나머지 구하기
    s = (_lst_v[-1]%1234567)
    
    return s
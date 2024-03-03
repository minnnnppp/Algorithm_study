def solution(s):
    cnt = 0
    # 1) length check
    if len(s) == 4 or len(s) == 6:
        cnt +=1
    
    # 2) check only int or str
    _lst = list(s)
    _lst_check = []
    for t in _lst:
        try: 
            _lst_check.append(int(t))
        except : pass
    if len(s) == len(_lst_check):
        cnt+=1
    
    if cnt == 2: return True
    else: return False
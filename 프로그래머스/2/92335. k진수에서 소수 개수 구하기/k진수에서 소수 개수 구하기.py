def solution(n, k):
    # 1. convert n
    answ1=""
    while n:            
        n, _t = divmod(n, k)
        answ1 = str(_t) + answ1  
    lst_word=answ1.split("0")  
    
    # 2. find pn
    cnt=0
    for _w in lst_word:
        if len(_w)==0 or int(_w)<2:    
            continue
        bool_pn=True
        for i in range(2,int(int(_w)**0.5)+1): # 소수찾기
            if int(_w)%i==0:
                bool_pn=False
                break
        if bool_pn:
            cnt+=1
            
    return cnt
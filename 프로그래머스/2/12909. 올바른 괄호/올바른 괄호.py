def solution(s):
    cnt = 0
    if s[0]=='(':
        for _s in s:
            if _s == '(':
                cnt +=1
            else:
                cnt -=1
                if cnt < 0:
                    return False
                
        if cnt == 0 and s[-1]==')':
            return True
        else: 
            return False
                
    else:
        return False
        
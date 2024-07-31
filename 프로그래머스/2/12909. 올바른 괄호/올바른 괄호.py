from collections import deque
def solution(s):
    # 1) s의 길이 홀수 체크
    if len(s)%2 == 1 :
        return False
    
    # 2) 첫번째, 마지막 괄호 체크
    if s[0] == ')' or s[-1] == '(':
        return False 
    
    lst_s = deque(list(s))
    wait = deque(list())
    answer = False
    
    # 3) 그 외의 경우
    while lst_s:
        if wait:
            _a = lst_s.popleft()
            _b = wait[-1]
            if _b == '(' and _a == ')':
                wait.pop()
                answer = True
            else:
                wait.append(_a)
        else:
            _b = lst_s.popleft()
            wait.append(_b)
            
    if wait:
        answer = False
            
    return answer
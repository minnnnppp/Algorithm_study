def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) >0:
                stack.pop()
            else:
                continue
    
    if len(stack) ==0:
        return True
    else:
        return False
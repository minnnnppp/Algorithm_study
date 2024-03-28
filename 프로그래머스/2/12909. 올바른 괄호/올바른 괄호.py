def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    
    return len(stack) == 0
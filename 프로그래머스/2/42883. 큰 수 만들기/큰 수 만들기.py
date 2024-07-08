def solution(number, k):
    stack=list()   
    
    for n in number:
        n = int(n)
        while k > 0 and stack and int(stack[-1]) < n:
            stack.pop()
            k -= 1
        stack.append(str(n))
        
    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)
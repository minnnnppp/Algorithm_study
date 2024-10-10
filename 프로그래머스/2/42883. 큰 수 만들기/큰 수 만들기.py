def solution(number, k):
    total_len = len(number)-k
    stack = []
    maxx = 0
    
    for i, n in enumerate(list(number)):
        while len(stack)>0 and int(stack[-1]) < int(n): 
            if len(stack)+len(number[i:]) > total_len:
                stack.pop()
            else:
                break
        else:
            if len(stack) == total_len:
                continue
            elif len(stack) > total_len:
                stack.pop()

        stack.append(n)
        
    return ''.join(stack)
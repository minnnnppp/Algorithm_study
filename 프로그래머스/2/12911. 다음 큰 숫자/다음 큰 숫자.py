def solution(n):
    cnt_1 = bin(n)[2:].count('1')
    target = n+1
    while True:
        if bin(target)[2:].count('1') == cnt_1:
            break
        else:
            target +=1
    
    return target
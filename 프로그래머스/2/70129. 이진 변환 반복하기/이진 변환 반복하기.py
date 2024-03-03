def solution(s):
    cnt = 0
    zeros = 0
    while s != '1':
        c = s.count('1')
        cnt += 1
        zeros += len(s) - c
        s = bin(c)[2:]
    
    return [cnt, zeros]
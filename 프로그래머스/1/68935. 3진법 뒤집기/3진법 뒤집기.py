def solution(n):
    answ = []
    while n > 0:
        n, s = divmod(n, 3)
        answ.append(str(s))
    
    return int(''.join(answ), 3)

    
def solution(n, times):
    times.sort()
    mint, maxt = 1, max(times)*n
    while mint <= maxt:
        midt = (maxt+mint)//2
        past = 0
        for t in times:
            past += midt//t
            if past == n:
                break
        if past >= n:
            sec = midt
            maxt = midt-1
        elif past < n:
            mint = midt+1
            
    return sec
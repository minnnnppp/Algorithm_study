def solution(routes):
    routes.sort()
    curr = routes[0]
    answ = 0
    
    for r in routes:
        if curr[1] >= r[0]:
            curr = [r[0], min(curr[1], r[1])]
        else:
            answ += 1
            curr = r
            
    
    return answ+1
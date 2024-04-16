def solution(sizes):
    max_l, max_w = 0, 0
    
    for s in sizes:
        w,l = s[0], s[1]
        maxx = max(w, l)
        minn = min(w, l)
        max_w = max(max_w,maxx)
        max_l = max(max_l, minn)
    
    return max_w*max_l
        
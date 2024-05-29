def solution(n, lost, reserve):
    # 1. make list of total student
    lost.sort()
    reserve.sort()
    target = [i for i in range(1, n+1)]
    # 2. find intersection between lost and reserve
    intersec = [x for x in lost if x in reserve]
    if intersec:
        lost = [x for x in lost if x not in intersec]
        reserve = [x for x in reserve if x not in intersec]
    
    # 3. consider if student can borrow extra uniform
    for i in range(1, n+1):
        if i in lost:
            target_bool = i in reserve
            if target_bool == True:
                lost.remove(i)
                reserve.remove(i)
            else:
                can = [x for x in [i-1, i+1] if x in reserve]
                if len(can) > 0:
                    reserve.remove(min(can))
                    lost.remove(i)
    
    return len([y for y in target if y not in lost])
    
    
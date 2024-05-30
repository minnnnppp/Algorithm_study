def solution(n, lost, reserve):
    # 1. 체육복 갖고 있는 학생 파악
    reserve_cp = [i for i in reserve if i not in lost]
    lost_cp = [x for x in lost if x not in reserve]
    reserve_cp.sort()
    
    # 2. 최종 분실 학생 집계해 체육복 보유 학생 수 계산
    for r in reserve_cp:
        b = r-1
        a = r+1
        if b in lost_cp:
            lost_cp.remove(b)
        elif a in lost_cp:
            lost_cp.remove(a)
    
    return n-len(lost_cp)
    
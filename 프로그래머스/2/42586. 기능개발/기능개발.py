import math
def solution(progresses, speeds):
    days = [math.ceil((100 - p)/s) for p, s in zip(progresses, speeds) ]
    target = []
    cnt, maxx = 1, days[0]
    for d in days[1:]:
        if d <= maxx:
            cnt+=1
        else:
            target.append(cnt)
            cnt = 1
            if d == days[-1]:
                continue
        maxx = max(maxx, d)
    target.append(cnt)

    return target
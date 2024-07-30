import math
def solution(progresses, speeds):
    nums = len(progresses)
    remains = [math.ceil((100-x)/s) for x, s in zip(progresses, speeds)]
    waits = [remains[0]]
    answ = []

    for r in remains[1:]:
        if max(waits) >= r:
            waits.append(r)
        else:
            answ.append(len(waits))
            waits = [r]

    if waits:
        answ.append(len(waits))
        
    return answ
            
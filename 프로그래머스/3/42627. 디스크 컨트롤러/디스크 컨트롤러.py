import heapq
def solution(jobs):
    total_time = sum([x[1] for x in jobs])
    complete = []
    answ = []
    sec = 0
    heapq.heapify(jobs)

    while sec < total_time:
        target = [x for x in jobs if (x[0] <= sec) and (x not in complete)]
        if jobs and target:
            target.sort(key = lambda x: x[1])

            sec += target[0][1]
            answ.append(sec-target[0][0])
            complete.append(target[0])
        else:
            sec += 1
        
    return sum(answ)//len(answ)
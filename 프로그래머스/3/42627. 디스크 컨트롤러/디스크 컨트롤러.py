import heapq
def solution(jobs):
    start, now, num, i = -1, 0, 0, 0
    answ = 0
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
            
        if len(heap)>0:
            _c = heapq.heappop(heap)
            start = now
            now += _c[0]
            answ += (now - _c[1])
            i+=1
        else:
            now+=1
        
    return int(answ/len(jobs))
def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    now = scoville[0]
    cnt = 0
    if now < K:
        while now < K and len(scoville)>1:
            mini = heapq.heappop(scoville)
            mini2 = heapq.heappop(scoville)
            target = mini + 2*mini2
            heapq.heappush(scoville, target)
            now = scoville[0]
            cnt+=1
    if now < K:
        return -1
    else: 
        return cnt   

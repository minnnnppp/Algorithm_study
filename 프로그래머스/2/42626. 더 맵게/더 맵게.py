import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if scoville and scoville[0] < K:
            if len(scoville)>1:
                x = heapq.heappop(scoville)
                y = heapq.heappop(scoville)
                heapq.heappush(scoville, (x+(2*y)))
                cnt += 1
            else:
                return -1
        else:
            return cnt
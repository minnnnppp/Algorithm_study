import heapq
def solution(operations):
    heap = []
    answer = []
    
    for x in operations:
        if x[0] == 'I':
            heapq.heappush(heap, int(x[2:]))
        else:
            if len(heap) == 0:
                pass
            elif x[2] == '-':
                heapq.heappop(heap)     # 자동정렬하니까 그냥 heap을 pop하면 최소값이 제거되는건가?
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    
    # heap에 숫자가 있으면 최대/최소값을 반환
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:       # heap에 숫자가 없으면 [0, 0]을 반환
        answer.append(0)
        answer.append(0)
    
    return answer
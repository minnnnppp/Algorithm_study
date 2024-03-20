import heapq
def solution(operations):
    heap = []          
    heap_max = []
    
    for o in operations:
        if o[0] == 'I':
            target = int(o.split(' ')[1])
            neg_target= (-1)*target
            heapq.heappush(heap, target)
            heapq.heappush(heap_max, (neg_target, target))
        elif o == 'D -1' and len(heap) >0 and len(heap_max)>0:
            target = heapq.heappop(heap)
            heap_max.remove(((-1)*target, target))
        elif o == 'D 1' and len(heap) >0 and len(heap_max)>0:
            target = heapq.heappop(heap_max)
            heap.remove(target[1])
            
    # res = [x for x in heap if (-x, x) in heap_max]
                               
    
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
    
    
    
    
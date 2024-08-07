import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    
    for x in operations:
        comm, num = x.split()
        num = int(num)
        
        ## 힙에 값 추가(최소/최대힙에 모두 추가)
        if comm == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-1)*(num))
        else:
            if num == -1:
                try: 
                    y = heapq.heappop(min_heap)
                    max_heap.remove((-1)*y)
                except IndexError:
                    pass
            else:
                try: 
                    y = heapq.heappop(max_heap)
                    min_heap.remove((-1)*y)
                except IndexError:
                    pass
                
    try : 
        return [max(min_heap), min(min_heap)]
    except:
        return [0, 0]
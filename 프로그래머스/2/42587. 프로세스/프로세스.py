def solution(priorities, location):
    queue = list(enumerate(priorities))
    cnt = 0
                            
    while True:
        target = queue.pop(0)
        if any(target[1] < x[1] for x in queue):
            queue.append(target)
        else:
            cnt += 1
            if target[0] == location:
                return cnt
        
            
            
            
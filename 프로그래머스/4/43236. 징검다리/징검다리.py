def solution(distance, rocks, n):
    left = 1
    right = distance
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        prev = 0
        for r in rocks:
            if (r-prev) < mid:
                cnt+=1
                if cnt > n:
                    break
            else:
                prev = r
        
        if cnt > n:
            right = mid-1
        else:
            answ = mid
            left = mid+1
            
    return answ
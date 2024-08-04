def solution(prices):
    answ = []
    for i in range(0, len(prices)):
        sec = 0
        
        for x in range(i+1, len(prices)):
            sec += 1
            if prices[i] > prices[x]:
                break
        
        answ.append(sec)
            
    return answ
                
            
        
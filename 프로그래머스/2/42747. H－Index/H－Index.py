def solution(citations):
    answer = 0
    for n in range(max(citations)+1, -1, -1):
        targets = [ x for x in citations if x >= n]
        if len(targets) >= n:
            return n
    
    return answer
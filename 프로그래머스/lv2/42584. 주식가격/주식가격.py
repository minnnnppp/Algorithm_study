from collections import deque
def solution(prices):
    queue = deque(prices)
    result = []
    
    while queue:
        price = queue.popleft()     # 맨 앞의 가격 pop
        sec = 0     # 초의 시작값 = 0초
        for q in queue:     # 돌아가면서 값 비교하기
            sec += 1        # 값 비교하면 일단 초가 1초 늘어나는 거니까 여기서 +1
            if price > q:   # 첫번째 값이 prices의 나머지 값보다 크면(=즉 가격이 하락하면)
                break           # 초 세는 거 중지
        result.append(sec)      # result 리스트에 sec 추가
    return result               # 결과 return
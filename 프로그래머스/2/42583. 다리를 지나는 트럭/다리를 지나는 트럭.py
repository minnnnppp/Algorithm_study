from collections import deque
def solution(bridge_length, weight, truck_weights):
    total_cnt = len(truck_weights)
    truck_weights = deque(truck_weights) 
    now = deque([])
    times = deque([])
    finish = []
    answ = 0

    while True:
        answ += 1
        ## 다 건넌 트럭 있는지 확인
        if now and answ - times[0] == bridge_length:
            finish.append(now.popleft())
            times.popleft()
            
            ### 모든 트럭이 통과하면 정답 반환
            if len(finish) == total_cnt:
                return answ

        ## 다리를 건널 트럭 있는지 확인
        if truck_weights and (sum(now)+truck_weights[0]<=weight):
            now.append(truck_weights.popleft())
            times.append(answ)
        
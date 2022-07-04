def solution(bridge_length, weight, truck_weights):
    # 시간 초기값 = 0
    time = 0
    q = [0] * bridge_length     # 다리에 올라갈 수 있는 트럭 수만큼 [0] 만들기
    
    # q가 있을 때까지? 반복
    while q:
        time += 1           # 1초 지나면
        q.pop(0)            # 차 한 대 나가고
        if truck_weights:       
            if sum(q) + truck_weights[0] <= weight: # 다리가 견딜 수 있는 무게가 트럭 무게 합보다 크거나 같을 경우
                q.append(truck_weights.pop(0))  # truck_weights의 첫번째 값을 빼고 q에 추가
            else:
                q.append(0)     # 트럭 무게 합을 다리가 견딜 수 없다면 q에 0 값을 추가하기
    return time
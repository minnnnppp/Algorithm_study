from collections import deque
def solution(bridge_length, weight, truck_weights):
    truckq = deque(truck_weights)
    iscnt = deque([0 for i in range(bridge_length)])
    sec, weightsum = 0, 0
    while True:
        if not truckq:
            return sec + bridge_length
        
        _minus = iscnt[0]
        _add = truckq[0]
        if weightsum - _minus + _add <= weight:
            weightsum = weightsum - _minus + _add
            iscnt.popleft()
            target = truckq.popleft()
            iscnt.append(target)
        else:
            weightsum -= _minus
            iscnt.popleft()
            iscnt.append(0)
        sec+=1
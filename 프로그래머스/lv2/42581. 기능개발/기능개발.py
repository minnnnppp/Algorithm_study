def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 100프로 완료되었다면
            progresses.pop(0)   # 추출해서
            speeds.pop(0)       
            count += 1          # 개수 카운팅하기
            
        else:
            if count > 0:       # 한 개 이상 완료되었다면
                answer.append(count)    # answer에 카운트를 반영해서 추가하고
                count = 0       # 카운트를 다시 0으로 만들기
            time += 1           # 아무것도 완료되지 않았다면 해당 작업의 작업 날짜만 하루 더하기
            
    answer.append(count)        # while문 반복 종료되면 마지막 카운트를 answer에 추가하기
    return answer
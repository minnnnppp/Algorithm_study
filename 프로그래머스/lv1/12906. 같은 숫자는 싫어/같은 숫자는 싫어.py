def solution(arr):
    answer = []
    answer.append(arr[0])           # 미리 0번째 값은 answer에 추가하고 시작
    
    for i in range(1, len(arr)):    # 1번부터 반복 시작
        if arr[i-1] != arr[i]:      # i-1, i가 서로 값이 같지 않은 경우
            answer.append(arr[i])   # 값 추가

    return answer
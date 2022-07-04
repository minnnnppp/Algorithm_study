from collections import deque

def solution(begin, target, words):
    if target not in words:  # 애초에 words에 target값이 없다면 return 0
        return 0

    q = deque()         
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()        # deque의 첫번째 값 추출

        if x == target:             # deque의 단어 = target 이면
            return cnt              # cnt 출력

        for i in range(0, len(words)):
            diff = 0                # words의 단어와 deque의 단어 간의 다른 알파벳 개수를 diff에 할당
            w = words[i]            
            for j in range(len(x)): # words의 길이만큼 w와 x의 알파벳 비교하기
                if x[j] != w[j]:    # j번째 알파벳이 서로 다르면
                    diff += 1       
            if diff == 1:           # 두 단어 간 알파벳이 하나만 다르다면
                q.append([w, cnt + 1])  # deque에 w를 추가하고 cnt+1하기
                
    return 0 # target값이 있으나 변환될 수 없는 경우 0d으로 반환
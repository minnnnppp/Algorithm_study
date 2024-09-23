def solution(name):
    cnt = 0
    minn = len(name)-1
    
    for i, n in enumerate(name):
        # 1) 최소 조작횟수 찾기: 정방향으로 조작 vs 반대방향으로 조작 횟수를 비교
        cnt += min(ord(n.upper())-ord('A'), ord('Z')-ord(n.upper())+1)
        
        # 2) 연속된 'A' 찾기
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 3) 이동 횟수의 최솟값 구하기
        minn = min([minn, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    
    return cnt + minn
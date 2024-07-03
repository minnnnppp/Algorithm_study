def solution(name):
    answ = 0
    # 기본 좌우이동 횟수
    min_move = len(name) - 1

    for _i, _s in enumerate(name):
        # 해당 문자의 변경횟수 최솟값 구하고 더해주기
        answ += min(ord(_s) - ord('A'), ord('Z') - ord(_s) + 1)

        # 해당 문자 이후 연속된 A 문자열 찾기
        nxt = _i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1

        # 기존, 연속된 A의 왼쪽부터 시작, 연속된 A의 오른쪽부터 시작 중 최솟값 찾음
        # 연속된 A가 여러 곳일 수 있으니 for문 동안에 갱신
        min_move = min([
            min_move, 
            2 *_i + len(name) - nxt, 
            _i + 2 * (len(name) -nxt)
        ])

    # 문자 변경 횟수 + 위치 이동 횟수
    answ += min_move
    
    return answ
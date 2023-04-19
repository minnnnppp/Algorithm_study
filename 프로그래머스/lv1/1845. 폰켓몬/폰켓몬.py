def solution(nums):
    # 가져갈 수 있는 폰켓몬 마리 수
    num_select = len(nums)//2
    # set으로 중복값 처리 후 num_select에 도달하기 전까지 서로 다른 종류의 수 계산
    cnt = 0
    for ele in set(nums):
        if cnt < num_select:
            cnt+=1
    return cnt
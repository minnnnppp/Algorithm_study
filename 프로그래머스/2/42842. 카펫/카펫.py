def solution(brown, yellow):
    total_size = brown + yellow
    # 노란색 카펫 약수 구하기
    y_divisors = [x for x in range(1, yellow+1) if yellow%x == 0]
    
    # 노란색이 중앙에 오는 경우의 가로*세로 구하기
    for x in y_divisors:
        y = yellow/x
        if (x+2)*(y+2) == total_size:
            return sorted([(x+2), (y+2)], reverse =True)
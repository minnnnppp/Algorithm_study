def solution(numbers):
    # 문자열 변환
    str_n = [str(x) for x in numbers] # 변환한 걸 리스트에 담음
    str_n.sort(key=lambda num: num*3, reverse=True) ## 1000 이하의 수를 가정했으니까
    return str(int(''.join(str_n)))
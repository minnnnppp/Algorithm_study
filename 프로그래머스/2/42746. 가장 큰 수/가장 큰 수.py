def solution(numbers):
    strs = sorted([str(x) for x in numbers], key = lambda x: x*3, reverse = True)
    return str(int(''.join(strs)))
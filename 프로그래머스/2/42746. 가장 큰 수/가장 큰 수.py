def solution(numbers):
    x = list(map(str, numbers))
    x.sort(reverse = True, key = lambda x: x*3)
    return str(int("".join(x)))
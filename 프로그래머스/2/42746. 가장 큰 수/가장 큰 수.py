def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key= lambda x: x*3, reverse=True)
    return str(int("".join(numbers)))
from itertools import permutations
def solution(numbers):
    lst_nums = list(numbers)
    combs = []
    cnt = 0
    
    # def make_int(n):
    #     answ = ''
    #     for i in range(len(n)):
    #         answ += n[i]
    #     return int(answ)

    def find_prime_num(n):
        if n <= 1:
            return False
        
        for i in range(2, num):
            if num%i == 0:
                return False
        
        return True

    for i in range(1, len(numbers)+1):
        _lst = set([int("".join(num)) for num in permutations(lst_nums, i)])
        for num in _lst:
            if num not in combs:
                if find_prime_num(num):
                    combs.append(num)
                    cnt+=1
    return cnt
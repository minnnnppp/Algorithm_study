from itertools import permutations
def solution(numbers):
    answs = list(numbers)
    for i in range(2, len(numbers)+1):
        _lst = list(permutations(numbers, i))
        _lst = [list(x) for x in _lst]
        _lst = [''.join(x) for x in _lst]
        answs += _lst
        
    def is_primenum(x):
        if x==0 or x==1:
            return False
        for i in range(2, x):
            if x%i == 0:
                return False
        return True
    
    set_answ = set([int(x) for x in answs if is_primenum(int(x))])
    return len(set_answ)
from itertools import product
def solution(word):
    answ = []       
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for x in product(vowels, repeat=i):
            answ.append(''.join(x))

    answ.sort()
    return answ.index(word)+1
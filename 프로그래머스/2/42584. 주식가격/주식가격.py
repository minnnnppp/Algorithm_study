# from collections import deque 
def solution(prices):
    length = len(prices)
    answ = []

    for x in range(length):
        y = x+1
        while y < length-1:
            if prices[x] > prices[y]:
                break
            y += 1 
        if y == length:
            sec = length-1-x
        else:
            sec = y-x
        answ.append(sec)
    return answ
def solution(arr):
    answ = [arr[0]]
    for n in arr:
        if n != answ[-1]:
            answ.append(n)
    
    return answ
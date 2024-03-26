def solution(arr):
    answ = []
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i+1]:
                answ.append(arr[i])
            answ.append(arr[i+1])
        else:
            if answ[-1]!= arr[i]:
                answ.append(arr[i])
    
    return answ
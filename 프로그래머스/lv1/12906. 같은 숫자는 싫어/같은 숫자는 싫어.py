def solution(arr):
    answ = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1] :
            if arr[i] not in answ:
                answ.append(arr[i])
            answ.append(arr[i+1])
        else:
            if arr[i] not in answ:
                answ.append(arr[i])
    
    return answ
            
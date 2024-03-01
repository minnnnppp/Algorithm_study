def solution(arr):
    answ = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            if i+1 != len(arr)-1:
                answ.append(arr[i])
            else:
                answ.append(arr[-2])
                answ.append(arr[-1])
            
        else:
            if i+1 == len(arr)-1:
                answ.append(arr[-1])
                
    return answ

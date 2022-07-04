def solution(array, commands):
    # commands에서 
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
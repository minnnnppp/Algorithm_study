def solution(nums):
    target_len = len(nums)//2
    uniq_len = len(set(nums))
    
    if uniq_len >= target_len:
        return target_len
    else:
        return uniq_len
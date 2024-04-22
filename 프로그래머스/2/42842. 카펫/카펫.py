def solution(brown, yellow):
    total_width = brown+yellow
    
    def find_factors(x):
        lst_factors = []
        for i in range(1, x+1):
            if x%i == 0:
                lst_factors.append(i)
        return lst_factors
    
    lst_tw_f = find_factors(total_width)
    for x in lst_tw_f:
        y = total_width//x
        if (x-2)*(y-2) == yellow:
            return [y, x]
        
    # mid_idx = (len(lst_tw_f)//2)
    # if (mid_idx//2 == 0):
    #     return [lst_tw_f[mid_idx], lst_tw_f[mid_idx]]
    # else:
    #     return [lst_tw_f[mid_idx], lst_tw_f[mid_idx-1]]
    
def solution(answers):
    dict_answ = {
        1: [1, 2, 3, 4, 5], 
        2: [2, 1, 2, 3, 2, 4, 2, 5], 
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    corrects_cnt = []
    
    for k, v in dict_answ.items():
        n = len(answers)//len(v)
        r = len(answers)%len(v)
        target = v*n + v[:r]
        corrects = [y for x, y in zip(target, answers) if x == y]
        corrects_cnt.append([k, len(corrects)])
    
    maxx = max(corrects_cnt, key = lambda x: x[1])[-1]
    
    return sorted([x[0] for x in corrects_cnt if x[1]==maxx])
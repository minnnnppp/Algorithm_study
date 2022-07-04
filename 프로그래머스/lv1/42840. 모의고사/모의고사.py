def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    res = []
    
    for i, ans in enumerate(answers):
        if ans == pattern1[i%len(pattern1)]:
            score[0]+=1
        if ans == pattern2[i%len(pattern2)]:
            score[1]+=1
        if ans == pattern3[i%len(pattern3)]:
            score[2]+=1
    
    for i, sco in enumerate(score):
        if sco == max(score):
            res.append(i+1)

    return res
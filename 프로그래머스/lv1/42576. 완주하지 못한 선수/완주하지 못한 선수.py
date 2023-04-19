import collections
def solution(participant, completion):
    answ = collections.Counter(participant) - collections.Counter(completion) 
    return list(answ.keys())[0]
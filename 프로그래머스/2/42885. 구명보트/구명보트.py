def solution(people, limit) :
    cnt = 0
    people.sort()

    f = 0
    e = len(people) - 1
    while f <= e :
        if people[e] + people[f] <= limit :
            f += 1
        e -= 1
        cnt += 1
    return cnt

def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[2])
    answ = 0
    path = set([costs[0][0]])

    while len(path) < n:
        for c in costs:
            if c[0] in path and c[1] in path:
                continue

            if c[0] in path or c[1] in path:
                path.update([c[0], c[1]])
                answ += c[2]
                break

    return answ
        
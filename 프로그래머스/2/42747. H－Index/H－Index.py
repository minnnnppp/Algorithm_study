def solution(citations):
    citations = sorted(citations, reverse = True)
    if max(citations) == 0:
        return 0
    else:
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
        return len(citations)
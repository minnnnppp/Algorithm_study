import collections
def solution(tickets):
    _dict = collections.defaultdict(list)
    for _path in sorted(tickets, key = lambda x: x[1]):
        _dict[_path[0]].append(_path[1])
    
    route = []
    
    def dfs(start):
        while _dict[start] :
            dfs(_dict[start].pop(0))
        route.append(start)
        
    dfs('ICN')
    
    return route[::-1]
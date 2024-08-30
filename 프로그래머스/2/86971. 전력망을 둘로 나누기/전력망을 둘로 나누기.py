# DFS 활용한 답안 공부
def solution(n, wires):
    answer = float("inf")
    def DFS(start, graph, visited, check_link):
        cnt = 1
        visited[start]=True                     # 일단 v 노드는 방문함
        for adj_v in graph[start]:              # v에 연결 되어있는 다른 노드에 대해 
            # 인접한 연결되어 있는 노드가 방문한 적 없으면 DFS 함수 호출해 탐색 가능한 노드 수 추가
            if visited[adj_v] == False and check_link[start][adj_v]:    
                cnt += DFS(adj_v, graph, visited, check_link)
        return cnt               


    # 끊은 간선인지 아닌지 체크하기 위한 리스트 
    check_link = [[True]*(n+1) for _ in range(n+1)] 
    graph = [[] for _ in range(n+1)]    # 송전탑 그래프 
    
    # 그래프 채우기 
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
        
    for a,b in wires:                               # 간선 정보를 다 확인하면서 
        visited = [False]*(n+1)                     # a, b 그룹의 붙어있는 송전탑 개수를 세기위해
        check_link[a][b] = False                    # a에서 b로 가는 간선을 끊어봄 
        cnt_a = DFS(a, graph, visited, check_link)  # 그때 a랑 붙어 있는 송전탑 개수 
        cnt_b = DFS(b, graph, visited, check_link)  # 그때 b랑 붙어 있는 송전탑 개수 
        check_link[a][b] = True                     # a와 b 사이 끊은 간선을 다시 붙임
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer
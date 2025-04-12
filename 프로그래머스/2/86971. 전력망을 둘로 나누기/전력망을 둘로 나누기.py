def make_graph(wires,n):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    return graph

from collections import deque

def bfs(s,graph,n):
    cnt=1# 연결된개수
    
    visited=[False]*(n+1)
    
    q=deque()
    q.append(s)
    visited[s]=True
    
    while q:
        # 송전탑 꺼내기
        cur=q.popleft()
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                visited[neighbor]=True
                q.append(neighbor)
                cnt+=1
    
    return cnt
    
def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        # i번째 노드 빼고 탐색 시행
        new_wires=wires[:i]+wires[i+1:]    
        graph=make_graph(new_wires,n) 
        cnt = bfs(1, graph, n)  # 아무 노드에서 bfs
        other=n-cnt #
        answer=min(answer,abs(cnt-other))
        
    return answer
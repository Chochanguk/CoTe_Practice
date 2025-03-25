from collections import deque
def bfs(s,n,graph):
    # 초기화
    queue=deque()
    visited=[False]*(n+1)
    distance=[0]*(n+1)
    
    # 초기 방문
    queue.append(s)
    visited[s]=True
    distance[s]=1

    while queue:
        # 현재 탐색 노드
        node = queue.popleft()
    
        # 현재 노드로부터 주변 탐색
        for neighbor in graph[node]:
            # 방문x
            if not visited[neighbor]:
                # 방문 처리
                visited[neighbor]=True
                queue.append(neighbor)
                distance[neighbor]=distance[node]+1
                
    return distance
    
    
def solution(n, edge):
    answer=0
    
    graph=[[] for _ in range(n+1)] # 빈 리스트 형성 => 연결된 노드만 추가
    
    # 인접 리스트 형성 (만약 노드가 비정형적이면 딕셔너리가 유리!)
    for n1,n2 in edge:
        # 양방향 연결
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    result=bfs(1,n,graph) # 1번 노드로부터 떨어진 거리를 반환
    
    print(result)
    max_distance=max(result)
    answer=result.count(max_distance)
    
    return answer

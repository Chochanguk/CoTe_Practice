from collections import deque

def bfs(s, n, graph):
    # 초기화
    queue = deque()
    # node가 1부터 시작하므로
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    # 1번 노드 방문 처리
    queue.append(s)
    visited[s] = True

    while queue:
        node = queue.popleft()
        # 해당 노드의 연결되어있는 노드들
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance

def solution(n, edge):
    # 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        # 양방향 연결
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)
    
    # BFS 실행
    result = bfs(1, n, graph)

    # 가장 멀리 떨어진 노드 개수 세기
    max_distance = max(result)
    return result.count(max_distance)

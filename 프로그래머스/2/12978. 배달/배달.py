import heapq as hq
def solution(N, road, K):
    '''
    1. 인접 리스트 방식으로 그래프 생성
       → 각 마을에 연결된 [도착 마을, 비용] 쌍 저장
    2. 거리 배열(dist) 및 우선순위 큐(heap) 초기화
       2.1. dist = [INF] * (N + 1): 1번 마을로부터 각 마을까지의 최단 거리
       2.2. dist[1] = 0: 시작 마을(1번)은 자기 자신까지의 거리 0
       2.3. heap = [(0, 1)]: (비용, 노드번호) 형태로 시작점 추가

    3. 다익스트라 알고리즘 실행 (Greedy + 우선순위 큐 기반)
       → 비용이 가장 적은 노드부터 탐색하며 거리 갱신

    4. heap에서 하나씩 꺼냄 (현재까지 누적 비용이 가장 낮은 노드)
    5. 해당 노드에서 연결된 모든 이웃 노드 탐색
       5.1. if dist[node] < cost:
            → 이미 더 짧은 경로로 방문한 적이 있으면 건너뜀
       5.2. new_cost = cost + weight:
            → 현재 노드를 거쳐 이웃 노드로 가는 새로운 비용 계산
       5.3. if new_cost < dist[next_node]:
            → 더 짧은 경로이면 거리 갱신하고 heap에 추가
    6. dist 배열 완성 후, 거리 ≤ K인 마을 수 세기

    '''
    answer=0
    
    # 그래프 초기화
    graph=[[] for _ in range(N+1)]
    for n1,n2,dist in road:
        graph[n1].append([n2,dist]) # n1 -> n2 가는 거리
        graph[n2].append([n1,dist]) # n2 -> n1 가는 거리
        
    print(graph)
    
    # 거리 초기화
    INF=float('inf')
    distances=[INF]*(N+1) # 1번 노드에서 각 노드 방문한 거리
    distances[1] = 0
    
    # 힙 초기화
    heapq=[[0,1]] # [ 이동 거리, 노드]: 노드까지 도달한 이동거리
    
    while heapq:
        dist, node =hq.heappop(heapq)
        
        # 만약 현재까지의 거리(dist)보다 더 적은 경로가 있었으면
        # 해당 노드로 방문해서 거리 갱신 x
        if distances[node]< dist:
            continue
        
        # 지금까지 가장 빠른 경로의 노드의 이웃들 탐색
        for neighbor, edge_dist in graph[node]:
            new_dist=dist +edge_dist # 기존 거리+간선
            
            # 새로 갱신한 거리가 해당 노드까지 방문한 거리보다 작으면 
            if new_dist < distances[neighbor]:
                # 거리 초기화 및 힙에 방문 노드 추가
                distances[neighbor]=new_dist
                hq.heappush(heapq,[new_dist,neighbor])
    
    answer=sum( 1 for dist in distances if dist<= K )
    
    return answer

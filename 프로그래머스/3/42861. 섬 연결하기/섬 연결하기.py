# 0. 가중치를 고려한 문제 풀이 BFS X => 최소 신장 트리(MST)

# # 1. 프림
# import heapq

# def solution(n, costs):
#     graph = [[] for _ in range(n)]
#     for a, b, cost in costs:
#         graph[a].append((cost, b))
#         graph[b].append((cost, a))

#     visited = [False] * n
#     min_heap = []
#     total_cost = 0

#     # 0번 노드부터 시작
#     visited[0] = True
#     for edge in graph[0]:
#         heapq.heappush(min_heap, edge)

#     while min_heap:
#         cost, node = heapq.heappop(min_heap)
#         if visited[node]:
#             continue
#         visited[node] = True
#         total_cost += cost
#         for next_cost, next_node in graph[node]:
#             if not visited[next_node]:
#                 heapq.heappush(min_heap, (next_cost, next_node))

#     return total_cost

# 2. 크루스칼 (Greedy 대표)


'''
크루스칼:
1. 가중치별로 간선을 정렬(낮은순부터)
2. union-find를 통해 MST 생성

union-find (크루스칼 핵심)
1. 두 노드(출발, 도착)가 같은 집합에 속해도 되는가? → 사이클 확인
2. 각 노드의 최상단 부모를 찾는다 → find
3. 두 노드의 최상단 부모가 다르면 → 다른 집합
4. 두 노드는 연결되어도 무방하므로 → 하나의 집합으로 union
5. (추가적으로 union이 True면 MST에 포함 가능)
'''

def find(parent, x):
    if parent[x] != x:
        # 다르면 재귀로 찾아냄
        parent[x] = find(parent,parent[x])  # 경로 압축
    return parent[x]    


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False

def solution(n, costs):
    # 1. 간선들을 가중치 기준으로 정렬
    costs.sort(key=lambda x: x[2])
    print(costs)
    
    
    # 2. Union-Find 초기화
    parent = [i for i in range(n)]

    # 3. 최소 신장 트리 비용 계산
    total_cost = 0
    edge_count = 0

    for a, b, cost in costs:
        if union(parent, a, b):  # 사이클이 없으면 연결
            total_cost += cost
            edge_count += 1
            if edge_count == n - 1:
                break  # MST 완성

    return total_cost

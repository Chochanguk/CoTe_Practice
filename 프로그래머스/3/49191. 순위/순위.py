from collections import deque

def bfs(s,n,graph):
    # 초기화 
    cnt=0
    queue=deque()
    visited=[False]*(n+1)
    # 방문 처리
    queue.append(s)
    visited[s]=True
    
    # 만약 s가 node를 이기고, node가 another을 이기면 s는 another을 이김
    while queue:
        node=queue.popleft()
        for another in graph[node]:
            if not visited[another]:
                queue.append(another)
                visited[another]=True
                cnt+=1
        
    return cnt

def solution(n, results):
    answer = 0 # 순위를 매길 수 있는 선수의 수
    
    '''
    순위를 알수 있는 방법
    본인이 확실히 이긴 횟수+ 본인이 확실히 진 횟수 =n-1 (자기자신:-1)
    (확실히 이긴 횟수는 자기 자신(S)이 A를 이겼을때, A가 B를 이기면 S는 B를 이김.)
    '''
    
    # 인접 리스트
    wins=[[] for _ in range(n+1)]
    defeats=[[] for _ in range(n+1)]
    
    for w,d in results:
        wins[w].append(d)
        defeats[d].append(w)

#     print("wins: ", wins)
#     print("defeats: ", defeats)

    for i in range(1,n+1):
        # 본인이 이기고, 진 횟수 
        
        win_cnt = bfs(i,n,wins)
        defeat_cnt = bfs(i,n,defeats)
        
        if win_cnt + defeat_cnt == n - 1:
            answer += 1
    
    return answer
from collections import deque
def bfs(n,m,maps):
    # print(n,m)
    # print(maps)
    
    # 초기화
    queue=deque()
    visited=[[False]*m for _ in range(n)]
    distance=[[0]*m for _ in range(n)]
    
    directions=[(-1,0),(1,0),(0,-1), (0,1)] # 동서 남북 
    
    # 첫방문
    queue.append((0,0)) # 초기위치
    visited[0][0]=True
    distance[0][0]=1
    
    while queue:
        x,y= queue.popleft() # 현재 위치

        for dx, dy in directions:
            nx,ny=x+dx,y+dy
            # 맵에 벗어나지 않았으며, 방문한 적 없고, 길인 경우에 이동 가능
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]==1:
                # 방문 처리
                queue.append((nx,ny))
                visited[nx][ny]=True
                distance[nx][ny]= distance[x][y]+1

    return distance[n-1][m-1]


def solution(maps):
    answer = -1
    '''
    1. n,m 구한다.
    2. (0,0) -> (n-1,m-1)
    3. 이동 가능은 길(1)이고, 맵의 크기를 벗어나지 않음
    4. 최단거리-> bfs 탐색
    5. 지나온 거리 return, 탐색 불가면 -1 return
    '''
    n=len(maps)    # 행의 크기
    m=len(maps[0]) # 열의 크기
    
    answer=bfs(n,m,maps)
    if answer==0:
        answer=-1
    
    return answer
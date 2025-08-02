from collections import deque

directions=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y,n,m,land,visited):
    cnt=1
    
    q=deque()
    same_list=[]
        
    # 방문 처리
    q.append((x,y)) 
    visited[x][y]=True
    same_list.append((x,y)) # 같은 영역인지 확인
    
    while q:
        cx,cy=q.popleft()
        
        for dx,dy in directions:
            nx,ny=cx+dx,cy+dy
            
            if 0<=nx<n and 0<=ny<m and land[nx][ny]==1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
                cnt+=1
                same_list.append((nx,ny))
                
    return cnt, visited,  same_list

def solution(land):
    answer = 0
    
    n=len(land)
    m=len(land[0])
    
    '''
    1. dict_land => x,y 를 키로 값을 땅 번호, 크기 설정
    
    1.1. dict_land[(x,y)]=[num, nubi]
    1.2. num개수 => num_cnt+1 만큼 visited를 False 처리
 
    
    2. 해당열의 행 하나씩 탐색
    2.1.  만약 해당 좌표의 땅을 탐색한 적이 있다면(DAT), 행 증가

    
    '''
    num=0
    
    land_visited=[[False]*m for _ in range(n)]
    dict_land=dict()
    
    
    # 1. bfs 탐색
    for i in range(n):
        for j in range(m):
            same_list=[]
            result=0
            if not land_visited[i][j] and land[i][j]==1:
                num+=1
                result, land_visited, same_list= bfs(i,j,n,m,land,land_visited)
                sl=len(same_list)
                for sx,sy in same_list:
                    dict_land[(sx,sy)]=[num,result]
                # print(same_list)
                # print(result)
                # print(num)
                # print()
    # print(dict_land)
    # print(num)
    
    for j in range(m):
        visited=[False]* (num+1) # 땅의 개수 만큼 비방문
        sum=0
        for i in range(n):
            
            if (i,j) in dict_land:
                cn, cnubi=dict_land[(i,j)]
                # 만약 현재 땅을 반문한적 없다면
                if not visited[cn]:
                    # 방문 처리
                    visited[cn]=True
                    sum+=cnubi
        answer=max(answer,sum)
    
    
    return answer
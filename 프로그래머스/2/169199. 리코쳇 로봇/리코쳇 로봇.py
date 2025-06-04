from collections import deque

def bfs(n,m ,sx,sy,ex,ey, board):
    
    visited=[[False]*m for _ in range(n)]
    q=deque()
    q.append((sx,sy,0)) # 초기 좌표, 거리
    
    visited[sx][sy]=True
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    
    while q: 
        x,y,d=q.popleft()
        
        # 목표 도달시 탐색 종료
        if (x,y) == (ex,ey):
            return d
        
        for dx,dy in directions:
            nx,ny=x,y
            
            # 벽까지 이동
            while True:
                # 1. 임시 한칸 이동
                tx,ty=nx+dx,ny+dy
                
                # 벽이거나 밖이면 해당 방향 탐색x
                if tx<0 or tx>=n or ty<0 or ty>=m or board[tx][ty]=='D':
                    break
                nx,ny= tx,ty # 이동
                
                
            # 방문한 적 없으면
            if not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny,d+1)) # 방향이 바껴야 증가
                
    # 도달x
    return -1
    
    

def solution(board):
    answer = 0
    n=len(board)
    m=len(board[0])
    
    
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                sx,sy=i,j
            if board[i][j]=='G':
                ex,ey=i,j
    answer= bfs(n,m ,sx,sy,ex,ey, board)
    return answer
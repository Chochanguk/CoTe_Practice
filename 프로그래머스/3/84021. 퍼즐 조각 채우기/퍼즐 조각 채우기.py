# 우회전 및 0,0 쪽으로 붙이기 
def rotate(shape):  
    new_shape=[]
    rotated=[]
    # 1. 회전
    for x,y in shape:
        rotated.append((y,-x))
    # 2. 회전한거 0,0 쪽으로 이동
    min_x,min_y=float('inf'),float('inf')
    
    for x,y in rotated:
        min_x, min_y=min(min_x,x),min(min_y,y)
    for x,y in rotated:
        new_shape.append((x-min_x, y-min_y))
        
    return sorted(new_shape)
    
    
from collections import deque

def make_shape(x,y,board,visited,target):
    # 세팅
    shape=[]
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    n=len(board)
    q=deque()
    # 초기화
    q.append((x,y))
    visited[x][y]=True
    shape.append((x,y))
    while q:
        x,y=q.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            # 범위내에 있고, 값이 0이면
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==target and not visited[nx][ny]:
                # 마지막 좌표에 넣고,
                shape.append((nx,ny))
                visited[nx][ny]=True
                q.append((nx,ny))
                
    # 0,0으로 붙이기
    min_x,min_y=float('inf'),float('inf')
    
    for x,y in shape:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    new_shape = []
    for x, y in shape:
        new_shape.append((x - min_x, y - min_y))
    
    return sorted(new_shape),visited # 모양과 방문 처리 갱신

#너비구하는 함수
def nubi(shape):
    return len(shape)
    


def solution(game_board, table):
    answer = 0
    '''
    풀이
    1. 빈칸의 도형 찾기
    2. 블록 도형 찾기
    3. 각 빈칸에 블록 맞는거 찾기
    3.1. 빈칸의 도형을 회전 시켜서 일치하는 도형이 있는지 찾기    
    
    '''
    n=len(game_board)
    shapes=[] # 빈칸의 모양들을 모음(0,0을 시점이며, 보드판에 표시)
    visited=[[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # 방문한적 없고, 빈칸이면 모양만들기
            if not visited[i][j] and game_board[i][j]==0:
                shape, visited = make_shape(i, j, game_board, visited,0)
                shapes.append(shape)
    blocks = []
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] == 1:
                block, visited = make_shape(i, j, table, visited,1)
                blocks.append(block)
    # 둘다 같이 0,0으로 근사한 좌표들
    print("shapes: ",shapes)
    print("blocks: ", blocks)
    # 하나씩 꺼내서 돌려 보고 같은지
    for block in blocks:
        rotated_block = block[:]

        for _ in range(4):  # 4번 회전
            rotated_block = rotate(rotated_block)

            if rotated_block in shapes:
                answer += nubi(rotated_block)
                shapes.remove(rotated_block)  # 사용한 빈칸 제거
                break  # 매칭 성공시 더 이상 회전 안함
            
    
    return answer
'''
maps = 직사각형
x:바다
1~9: 무인도의 식량
상, 하, 좌, 우로 연결 => 무인도
각 무인도의 식량의 합 => 최대 며칠 생존 가능한지

각 섬에서 최대 며칠씩 머무룰 수 있는지 배열에 오름차순으로 담아 리턴

'''
from collections import deque
def bfs(n, m, sx, sy, visited, directions, maps):
    total_foods=int(maps[sx][sy]) # 식량 총합
    
    q=deque()
    visited[sx][sy]=True
    q.append((sx,sy))
    
    while q:
        x,y=q.popleft()     
        
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] != 'X':
                
                q.append((nx,ny))
                visited[nx][ny]=True
                total_foods+=int(maps[nx][ny])
    
    return total_foods


def solution(maps):
    answer = []
    
    
    
    n=len(maps)
    m=len(maps[0])
    visited=[[False]*m for _ in range(n)]
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(n,m,i, j,visited, directions,maps))
    
    answer.sort()
    # print('answer: ', answer)
    if not answer:
        return [-1]
    else:
        return answer

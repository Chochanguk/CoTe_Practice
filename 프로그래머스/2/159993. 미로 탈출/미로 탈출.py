from collections import deque

# 시점 -> 종점 이동
def bfs(maps, start, target):
    n, m = len(maps), len(maps[0])
    distance = [[-1]*m for _ in range(n)]
    q = deque()

    x, y = start
    distance[x][y] = 0
    q.append((x, y))

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        x, y = q.popleft()
        if (x, y) == target:
            return distance[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 'X' and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i, j)
            elif maps[i][j] == 'L':
                l = (i, j)
            elif maps[i][j] == 'E':
                e = (i, j)
    
    to_lever = bfs(maps, s, l)
    to_exit = bfs(maps, l, e)
    
    # 레버를 안지나쳤거나 종점이 -1 이면 return -1
    if to_lever == -1 or to_exit == -1:
        return -1
    
    # 이동 거리합
    return to_lever + to_exit

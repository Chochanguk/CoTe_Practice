from collections import deque

directions= [(1,0),(-1,0),(0,1),(0,-1)]
def get_path(sx, sy, ex, ey):
    path = [(sx, sy)]
    x, y = sx, sy
    while x != ex:
        x += 1 if x < ex else -1
        path.append((x, y))
    while y != ey:
        y += 1 if y < ey else -1
        path.append((x, y))
    return path
    

def solution(points, routes):
    answer = 0

    '''
    1. 로봇마다 모든 이동 경로를 구함
    2. 이동경로마다 
    '''
    point_dict=dict()
    pnum=0
    max_px=0
    max_py=0
    
    for point in points:
        x,y=point[0],point[1]
        
        if x>=max_px: max_px=x
        if y>=max_py: max_py=y
        
        
        point_dict[pnum]=(x-1,y-1)
        pnum+=1

    
    paths=[]
    
    n=len(routes)
    m=len(routes[0])
    
    # print(bfs (0,1, 1,0))
    path_list=[]
    for i in range(n):
        sx,sy=point_dict[routes[i][0]-1]
        paths=[]
        for j in range(1, m):
            
            tx,ty=point_dict[routes[i][j]-1] # 타켓 지점
            path=get_path(sx, sy, tx, ty)
            if j == 1:
                # 첫 구간은 시작점 포함해서 다 넣어야 함
                paths.extend(path)
            else:
                # 이후는 시작점이 이전 경로의 도착점이므로 제외
                paths.extend(path[1:])
            sx,sy=tx,ty
        path_list.append(paths)
    
    # 패딩
    l_list=[]
    for i in range(n):
        l_list.append(len(path_list[i]))
    max_l=max(l_list)    
    # print(l_list)
    
    for i in range(n):
        cpath=path_list[i]
        cl=len(cpath) # 현재 길이
        if cl<max_l:
            padding=[(-1,-1)]*(max_l- cl)
            path_list[i].extend(padding)
    
    # for i in range(n):
    #     print(path_list[i])
    #     print()
    
    for t in range(max_l):
        pos_dict = {}
        for i in range(n):
            pos = path_list[i][t]
            if pos == (-1, -1):
                continue
            if pos not in pos_dict:
                pos_dict[pos] = 0
            pos_dict[pos] += 1

        for cnt in pos_dict.values():
            if cnt >= 2:
                answer += 1  # 그 시간에 그 좌표에서만 1번 충돌로 간주


    return answer

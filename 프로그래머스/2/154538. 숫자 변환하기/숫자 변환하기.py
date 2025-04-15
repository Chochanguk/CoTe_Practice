# 1. bfs 탐색
from collections import deque

def bfs(x, y, n):
    q = deque()
    q.append((x,0))  # (현재 값, 연산 횟수)

    visited = set()
    visited.add(x)
    
    while q:
        x,distance= q.popleft()
        # 같은 값이면 bfs 탐색 종료
        if x == y:
            return distance
        
        for nx in (x + n, x * 2, x * 3):

            if nx not in visited and nx <= y:
                q.append((nx,distance+1))
                visited.add(nx)
    return -1


def solution(x, y, n):
    return bfs(x, y, n)


# # 2. dfs 로 탐색 하는 법 => 비효율(최소값 보장을 위해 모든 경우 탐색)
# def dfs(x, y, n, cnt, cnt_list):
#     # print(x)
#     if x == y:
#         cnt_list.append(cnt)
#         return
#     if x > y:
#         return
#     # 경우의 수 다 탐색
#     dfs(x + n, y, n, cnt + 1, cnt_list) # 5,10,15,25,30,35,40
#     dfs(x * 2, y, n, cnt + 1, cnt_list) # 35*2, 30*2, ...
#     dfs(x * 3, y, n, cnt + 1, cnt_list) # 35*3, 30*3, ... 
    

# def solution(x, y, n):
#     cnt_list = []
#     dfs(x, y, n, 0, cnt_list)
#     # print(cnt_list)
#     return min(cnt_list) if cnt_list else -1

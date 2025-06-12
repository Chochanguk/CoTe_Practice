import copy

# 방향: ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

'''
-> 물고기는 번호가 작은 순(1~16) 부터 한칸 이동.
-> 각 물고기는 방향 이동할 수 있는 칸 탐색.
->-> 이동 가능 칸 탐색시 현재 방향에서 반시계 회전
->> 이동 불가능하면 이동x
->>  물고기에서 다른 물고기 이동시 서로 위치 변경
->-> 이동 가능: 빈칸 or 다른 물고기가 있는 칸
->-> 이동x: 공간의 경계를 넘거나 상어가 있는 칸

풀이
1. 복사 하지 않고, 이동 후에는 갱신해야함.
2. 갱신한걸 바탕으로 이동해야함 
'''


# def fish_move(board, fish_info):
#
#     for cur_fish in range(1,17):
#         x,y,direction,alive=fish_info[cur_fish]
#         # 살아 있는 애만 이동
#         if not alive:
#             continue
#         # 1. 반시계 방향 탐색
#         for d in range(8):
#             nd=(direction+d)%8
#             nx,ny=x+dx[nd],y+dy[nd]
#             # 2. 이동 가능하면 이동
#             if 0<=nx<4 and 0<=ny<4 and board[nx][ny]!=-1:
#                 # 3. 물고기끼리 위치 변환
#                 if board[nx][ny]!=0:
#                     next_fish = board[nx][ny]  # 그 다음 물고기 값
#                     fish_info[next_fish][0], fish_info[next_fish][1]=x,y # 현재 값으로 변경(방향 전환x)
#                     board[x][y]=next_fish
#                 else:
#                     board[x][y] = 0
#                 fish_info[cur_fish]=[nx,ny,nd,True]
#                 board[nx][ny] = cur_fish
#                 break # 이동 방향 찾으면 반복문 종료
#     # #
#     # print()
#     # print("==== 이동 후 물고기 정보 ====")
#     # print(fish_info)
#     # print("==== 이동 후 정보 ====")
#     # print(board)
#
#     return board,fish_info

def fish_move(board, fish_info):
    for cur_fish in range(1, 17):

        x, y, direction, alive = fish_info[cur_fish]
        # 살아 있는 애만 이동
        if not alive:
            continue
        # 1. 반시계 방향 탐색
        for d in range(8):
            nd = (direction + d) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            # 2. 이동 가능하면 이동
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != -1:
                next_fish = board[nx][ny]  # 그 다음 물고기 값
                # 3. 물고기끼리 위치 변환
                if next_fish != 0:
                    fish_info[next_fish][0], fish_info[next_fish][1] = x, y  # 현재 값으로 변경(방향 전환x)
                board[nx][ny], board[x][y] = cur_fish, next_fish
                fish_info[cur_fish] = [nx, ny, nd, True]
                break  # 이동 방향 찾으면 반복문 종료
    #
    # print()
    # print("==== 이동 후 물고기 정보 ====")
    # print(fish_info)
    # print("==== 이동 후 정보 ====")
    # print(board)

    return board, fish_info


'''
3. 물고기 이동 후 상어 이동
-> 한번에 여러 개 칸 이동 가능(백트래킹 탐색)
->-> 이동 중 지나카는 칸의 물고기는 안먹음
->-> 물고기가 없는 칸으로는 이동x
->> 해당 방향으로 물고기 탐색시 없으면 집으로 이동

'''


# 상어가 이동 가능한 위치 반환
def shark_moving_position(shark_x, shark_y, shark_d, board):
    positions = []  # 상어가 이동 가능한 좌표들 모음 [(x,y)...]

    for i in range(1, 4):  # 1~3번
        nx, ny = shark_x + dx[shark_d] * i, shark_y + dy[shark_d] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] > 0:
            positions.append((nx, ny))

    # print()
    # print("==== 상어 이동 가능 정보 ====")
    # print( positions)

    return positions


def dfs(shark_x, shark_y, board, fish_info, total):
    global result

    board = copy.deepcopy(board)
    fish_info = copy.deepcopy(fish_info)

    # 1. 먼저 잡아 먹음
    target = board[shark_x][shark_y]
    shark_d = fish_info[target][2]  # 상어 방향 갱신
    total += target  # 잡아 먹었으므로 값 갱신
    # 1.2. 값 갱신
    fish_info[target][3] = False
    board[shark_x][shark_y] = -1

    # 2. 물고기 이동
    new_board, new_fish_info = fish_move(board, fish_info)

    # 3. 상어 이동
    # 3.1. 상어 이동 방향 체크
    positions = shark_moving_position(shark_x, shark_y, shark_d, new_board)

    # 3.2. 상어 이동 불가능하면 재귀(탐색) 종료
    if not positions:
        result = max(result, total)
        return

    # 3.3. 상어 이동 가능
    for nx, ny in positions:
        # 이전 값은 빈칸 처리
        board[shark_x][shark_y] = 0
        dfs(nx, ny, board, fish_info, total)


# 입력
board = [[0] * 4 for _ in range(4)]
fish_info = dict()
for i in range(1, 17):
    fish_info[i] = [-1, -1, -1, True]  # x,y,d,alive
for i in range(4):
    col = 0
    fishes_datas = list(map(int, input().split()))
    for j in range(0, len(fishes_datas), 2):
        num = fishes_datas[j]  # 짝수
        d = fishes_datas[j + 1] - 1
        fish_info[num][0], fish_info[num][1], fish_info[num][2] = i, col, d
        board[i][col] = num
        col += 1  # 열 증가

# 상어 (0,0)

# print()
# print("==== 초기 물고기 정보 ====")
# print(fish_info)
# print("==== 보드판 정보 ====")
# print(board)

result = 0
# 상어 (0,0)
dfs(0, 0, board, fish_info, 0)


print(result)
def solution(n):
    '''
    직각 삼각형으로 만들어서 해결
    1. 아래, 오른쪽, 왼쪽 대각선 이동
    2. nxn 격자판 생성
    3. 범위를 벗어나거나 이미 채워진 곳(방무처리 된)이라면 방향 전환
    4. 
    '''
    
    directions = [(1, 0), (0, 1), (-1, -1)]  # 아래 → 오른쪽 → 대각선 위
    board = [[0] * n for _ in range(n)]

    x, y = 0, 0
    num = 1
    max_num = n * (n + 1) // 2  # 삼각형 총 개수(직삼각형 너비)
    
    dir_idx = 0  # 방향 인덱스
    board[x][y]=num
    
    while num < max_num:

        # 다음 좌표 계산
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy

        # 범위를 벗어나거나 이미 채워진 곳이라면 방향 전환
        if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] != 0:
            # 다음 좌표 갱신
            dir_idx = (dir_idx + 1) % 3
        else:
            board[nx][ny] = board[x][y]+1
            num+=1
            x,y=nx,ny

    # 결과를 한 줄로 이어서 반환
    result = []
    for i in range(n):
        for j in range(i + 1):  # 삼각형 모양만 가져오기
            result.append(board[i][j])
    return result

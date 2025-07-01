def solution(board):
    n = len(board)
    m = len(board[0])
    max_size = 0

    # 기존 board를 복사 (깊은 복사)
    temp = [[board[i][j] for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                temp[i][j] = min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1]) + 1
                max_size = max(max_size, temp[i][j])

    # 가장 큰 정사각형이 맨 첫 줄/열에 있을 경우를 위해 예외 처리
    if max_size == 0:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    return 1
        return 0

    return max_size * max_size

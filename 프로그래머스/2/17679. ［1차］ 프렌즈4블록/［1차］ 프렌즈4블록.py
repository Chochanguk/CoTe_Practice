def broute_force(m, n, board):
    removed = set()

    # 2x2 블록 확인
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != '0' and \
               board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                removed |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}

    cnt = len(removed)

    # 제거
    for x, y in removed:
        board[x][y] = '0'

    # 아래로 떨어뜨리기
    for j in range(n):
        col = [board[i][j] for i in range(m) if board[i][j] != '0']
        for i in range(m - len(col)):
            board[i][j] = '0'
        for i in range(len(col)):
            board[m - len(col) + i][j] = col[i]

    return cnt, board

def solution(m, n, board):
    board = [list(row) for row in board]
    total = 0

    while True:
        cnt, board = broute_force(m, n, board)
        if cnt == 0:
            break
        total += cnt

    return total

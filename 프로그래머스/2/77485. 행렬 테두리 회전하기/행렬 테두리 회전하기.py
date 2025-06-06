from collections import deque

def rotate(n, m, x1, y1, x2, y2, board):
    q = deque()

    # 테두리 값을 순서대로 모으기
    for i in range(y1, y2):
        q.append(board[x1][i])
    for i in range(x1, x2):
        q.append(board[i][y2])
    for i in range(y2, y1, -1):
        q.append(board[x2][i])
    for i in range(x2, x1, -1):
        q.append(board[i][y1])


    
    q.rotate(1)  # 시계 방향 한 칸 회전

    
    # 최소값 찾기
    min_n = min(q)

    # 회전된 값 다시 넣기
    for i in range(y1, y2):
        board[x1][i] = q.popleft()
    for i in range(x1, x2):
        board[i][y2] = q.popleft()
    for i in range(y2, y1, -1):
        board[x2][i] = q.popleft()
    for i in range(x2, x1, -1):
        board[i][y1] = q.popleft()

    return min_n

def solution(rows, columns, queries):
    answer = []
    n, m = rows, columns
    board = [[i * m + j + 1 for j in range(m)] for i in range(n)]

    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        min_n = rotate(n, m, x1, y1, x2, y2, board)
        answer.append(min_n)
    
    return answer

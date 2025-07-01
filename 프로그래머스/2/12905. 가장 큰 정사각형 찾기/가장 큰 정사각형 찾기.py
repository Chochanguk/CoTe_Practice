from copy import deepcopy

def solution(board):
    n = len(board)
    m = len(board[0])
    max_size = 0

    # 기존 board를 복사 (깊은 복사)
    temp=deepcopy(board)
    idx=0
    for i in range(1, n):
        for j in range(1, m):
            # (i, j)가 정사각형의 오른쪽 아래 꼭짓점이라고 가정
            if board[i][j] == 1:
                # 현재 표의 이전 좌표에서 가장 작은 값에+1로 갱신
                # => 현재 정사각형의 한변의 길이로
                temp[i][j] = min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1]) + 1
                max_size = max(max_size, temp[i][j])
#             idx+=1
#             print(f"===={idx} 번째:{i},{j}====")
#             print(temp)
#             print()
            
    # 가장 큰 정사각형이 맨 첫 줄/열에 있을 경우를 위해 예외 처리
    if max_size == 0:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    return 1
        return 0

    return max_size * max_size

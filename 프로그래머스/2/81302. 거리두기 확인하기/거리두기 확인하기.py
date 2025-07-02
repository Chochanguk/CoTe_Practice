def is_ok(board, players):
    n = len(players)
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = players[i]
            x2, y2 = players[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            
            # 거리가 2이상이면 패스
            if dist > 2:
                continue

            # 맨해튼 거리 1 = 무조건 거리두기 실패
            if dist == 1:
                return 0

            # 맨해튼 거리 2인 경우
            if x1 == x2:
                # 같은 행 => 사이에 칸막이 있는지 확인
                if board[x1][(y1 + y2)//2] != 'X':
                    return 0
            elif y1 == y2:
                # 같은 열
                if board[(x1 + x2)//2][y1] != 'X':
                    return 0
            else:
                # 양 옆 두 칸 모두 확인
                if board[x1][y2] != 'X' or board[x2][y1] != 'X':
                    return 0
    return 1

def solution(places):
    answer = []

    # 각 대기실 별 시뮬레이션
    for place in places:
        print("=== 시뮬레이션 시작 ====")
        
        #1. 2차원 격자판
        board=[]
        for infos in place:
            row=list(infos)
            board.append(row)
                           
        players=[] #플레이어들의 좌표            
        for i in range(5):
            for j in range(5):
                if board[i][j]=='P':
                    players.append((i,j))
        print()
        print(f'플레이어들: {players}')
        #2. 격자판에서 맞는지 확인
        answer.append(is_ok(board,players))
        
        
        
        
    return answer
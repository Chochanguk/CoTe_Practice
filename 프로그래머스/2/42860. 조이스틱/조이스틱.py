def solution(name):
    answer = 0
    n = len(name)
    
    # 1. 알파벳 변경 비용 먼저 계산
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
    
    # 2. 커서 이동 최소값 계산
    min_move = n - 1  # 최악의 경우: 그냥 오른쪽으로 끝까지
    
    for i in range(n):
        next_i = i + 1
        # 다음 문자가 A일 때 얼마나 연속되는지 확인
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # i까지 갔다가 → 뒤로 돌아가는 경우 or
        # 뒤까지 갔다가 → 앞으로 오는 경우 비교
        move = i + n - next_i + min(i, n - next_i)
        min_move = min(min_move, move)

    answer += min_move
    return answer

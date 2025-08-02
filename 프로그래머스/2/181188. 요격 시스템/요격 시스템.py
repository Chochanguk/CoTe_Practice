def solution(targets):
    # 끝나는 시점 기준 정렬
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_shot = -1  # 마지막 요격 지점
    
    # print(targets)
    
    for start, end in targets:
        # 이전 요격 위치로 이 타겟을 커버할 수 없다면 새 요격
        if last_shot < start:
            answer += 1
            last_shot = end - 1  # 구간 내 가장 마지막 위치에서 발사
            
    return answer

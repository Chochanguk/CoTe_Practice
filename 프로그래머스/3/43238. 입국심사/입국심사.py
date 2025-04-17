def solution(n, times):
    left = min(times)  * 1  # 최소 걸린 시간(한명)
    right = max(times) * n  # 최악의 경우 시간 (심사관 수)
    
    answer = right

    while left <= right:
        # 중앙 시간
        mid = (left + right) // 2
        
        # 처리 가능한 사람을 가정
        total = sum(mid // time for time in times)
        
        # 만약 처리 가능한 사람이 더 많게 나오면 우측 감소
        if total >= n:
            answer = mid
            right = mid - 1
            
        # 만약 처리 가능한 사람이 더 적게 나오면 좌측 증가
        else:
            left = mid + 1

    return answer

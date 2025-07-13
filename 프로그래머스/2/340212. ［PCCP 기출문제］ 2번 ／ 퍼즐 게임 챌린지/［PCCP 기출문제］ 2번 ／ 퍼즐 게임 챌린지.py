'''
1. n개의 퍼즐을 제한 시간 내에 풀어야 함.
2. 숙련도에 따라 퍼즐을 풀 때 틀리는 횟수가 바뀜
3. 현재 퍼즐의 난이도를 diff, 소요시간: time_cur 
3.1. 이전 퍼즐 소요시간: time_preve, 숙련도: level

4.
diff<=level -> time_cur 만큼 시간 사용
diff > level 
4.1. diff-level 번 틀림
틀리 때마다 time_cur 만큼 시간 사용 및
time_prev 만큼 사용해서 이전 퍼즐을 풀어야 함.(무조건 정답 처리)
diff-level 틀린 이후 time_cur만큼 시간 사용해서 해결

=(diff-level)*(time_cur+time_prev) + time_cur

5. 퍼즐게임에는 전체 제한시간: limit 
6. 제한 시간 내 퍼즐을 해결하기 위한 숙련도 최솟값 계산

'''
# 난이도가 더 높은 값 계산
def under_diff(diff, level,time_cur,time_prev):
    return (diff-level)*(time_cur+time_prev) + time_cur

def is_possible(level, diffs, times, limit,l):
    total_time = times[0]
    
    for i in range(1,l):
        diff=diffs[i]
        time_cur=times[i]
        time_prev=times[i-1]
        
        if diff>level:
            total_time+=under_diff(diff, level,time_cur,time_prev)
        else:
            total_time+=time_cur
    
    if total_time <= limit:
        return True
    else:
        return False

    
    

def solution(diffs, times, limit):
    answer = -1
    max_level=max(diffs) # 최대값
    l=len(diffs)
    
    # 1개이면 숙련도 1 반환
    if l == 1:
        if times[0] <= limit:
            return 1
        else:
            return -1  # 아무리 높은 레벨이어도 못 품
    left,right=1, max_level
    
    # 이진 탐색 : O(n log(max_level)
    while left<=right:
        
        mid=(left+right)//2
        
        # 가능하면 정답을 고치고 우측에서 한번 더 체크 
        if is_possible(mid, diffs, times, limit, l):
            answer=mid
            right=mid-1 # 더 낮음 레벨 필요
        else:
            left=mid+1 # 더 높은 레벨 필요
        

    return answer
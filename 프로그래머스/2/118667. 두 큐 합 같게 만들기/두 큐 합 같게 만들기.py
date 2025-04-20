from collections import deque

def solution(queue1, queue2):
    '''
    그리디로 해결.
    우선 두수의 목표보다 크면 빼고 집어넣음.
    그 수의 합을 갱신하면서 반복문을 수행
    
    '''
    total_sum = sum(queue1) + sum(queue2)
    # 합이 홀수면 두 큐의 합 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1
    target = total_sum // 2

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # 두 큐를 하나의 리스트로 간주하고 index 이동으로 해결
    n = len(queue1)
    max_count = n * 3  # worst case: 3n번 이내에 해결 안 되면 -1
    count = 0
    p1, p2 = 0, 0  # p1: q1의 앞에서 제거할 위치, p2: q2의 앞에서 제거할 위치
    
    while count <= max_count:
        # 타켓에 도달하면 반복문 종료
        if sum1 == target:
            return count
        # 첫번째 큐의 합이 타겟보다 크면
        elif sum1 > target:
            # 큐에서 꺼내서 집어넣음
            val = q1.popleft()
            sum1 -= val
            q2.append(val)
            sum2 += val
        # 두번째 큐의 합이 타겟보다 크면
        else:
            val = q2.popleft()
            sum2 -= val
            q1.append(val)
            sum1 += val
        # 작업 시행
        count += 1

    return -1

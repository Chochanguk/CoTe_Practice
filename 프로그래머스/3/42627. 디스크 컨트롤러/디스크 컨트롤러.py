import heapq as hq

def solution(jobs):
    answer = 0
    
    wait = []  # 요청 대기 큐 (요청시각, 작업시간, 작업번호) => 요청시각이 빠른순
    ready = []  # 작업 가능 큐 (작업시간, 요청시각, 작업번호 => 우선 순위 순
    
    worked_s = {}  # 작업 요청 시각
    worked_t = {}  # 작업 종료 시각 기록
    # 1. wait 큐에 대기
    for num, job in enumerate(jobs):
        hq.heappush(wait, (job[0], job[1], num))
        worked_s[num] = job[0]
        worked_t[num] = -1
    print(wait)
    
    # 2. 현재 작업 중인 프로세스와 시뮬레이션 변수 초기화
    working = [-1, -1]  # [작업번호, 남은 작업 시간]
    time = 0
    n = 0
    
    # 모든 작업을 했는지 확인
    while n < len(jobs):
        
        # 요청된 작업을 ready로 이동
        # 대기큐에 값이 있고, 대기큐 맨 앞의 요청 시각이 현재 시각보다 작으면
        while wait and wait[0][0] <= time:
            req, dur, num = hq.heappop(wait)
            hq.heappush(ready, (dur, req, num))

        num, left_t = working

        # 현재 작업 중이 아니라면
        if left_t == -1:
            if ready:
                dur, req, num = hq.heappop(ready)
                working = [num, dur - 1]  # 첫 1초는 바로 처리
                if dur == 1:
                    worked_t[num] = time + 1  # 현재 시간에 완료됨
                    working = [-1, -1]
                    n += 1
        else:
            working[1] -= 1
            if working[1] == 0:
                worked_t[working[0]] = time + 1  # 작업 완료 시간 기록
                working = [-1, -1]
                n += 1

        time += 1  # 시간은 루프 마지막에 증가

    # 평균 시간 계산
    total = 0
    for num in worked_t:
        total += worked_t[num] - worked_s[num]

    answer = total // len(jobs)
    return answer

def solution(plans):
    answer = []
    
    # 시작 시간을 분 단위로 변환하고 정렬
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        plan[1] = h * 60 + m
        plan[2] = int(plan[2])
    
    plans.sort(key=lambda x: x[1])
    
    stack = []  # 멈춘 과제 [과제명, 남은 시간]
    now = plans[0][1]  # 현재 시간
    
    for i in range(len(plans) - 1):
        name, start, duration = plans[i]
        next_start = plans[i + 1][1] # 다음 시작 시각
        time_available = next_start - start # 현재 재생 가능 시각

        # 만약 과제를 못끝내면 스택에 집어넣음
        if duration > time_available:
            # 과제를 끝내지 못함
            stack.append([name, duration - time_available])
        # 만약 과제를 끝내면
        else:
            # 1. 정답에 넣음
            answer.append(name)
            # 2. 현재 시각 갱신
            now = start + duration
            # 3. 다음 까지 실행있는가
            time_left = next_start - now
            # 4. 스택도 있고, 다음 거 까지 실행할 시각이 남아 있으면 계속 스택에서 빼서 실행
            while stack and time_left > 0:
                s_name, s_duration = stack.pop()
                if s_duration <= time_left:
                    answer.append(s_name)
                    time_left -= s_duration
                    now += s_duration
                else:
                    # 다 못 끝내면 다시 스택에 넣기
                    stack.append([s_name, s_duration - time_left])
                    break

    # 마지막 과제는 무조건 새로 시작하므로 바로 추가
    answer.append(plans[-1][0])

    # 남은 스택 처리
    while stack:
        answer.append(stack.pop()[0])
        
    return answer

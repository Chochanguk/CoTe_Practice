def make_sec(book_time):
    after_sec = []
    for bt in book_time:
        start, end = bt[0], bt[1]

        # 시작 초, 종료 초
        s_sec = int(start[:2]) * 60 + int(start[3:])
        e_sec = int(end[:2]) * 60 + int(end[3:]) + 10  # 청소 시간 10분 추가

        after_sec.append([s_sec, e_sec])
    return after_sec


def solution(book_time):
    answer = 0
    book_sec = make_sec(book_time)

    # 시작 시간 기준으로 오름차순 정렬
    book_sec.sort(key=lambda x: x[0])
    
    rooms=[] # 방 배열(각 방별로 [시작,종료] )
    
    # 예약 시각 하나씩 꺼냄
    for reserving in book_sec:
        start,end=reserving
        # 방을 새로 만드는지 확인
        is_reserved=False 
        print(start,end)
        
        for room_booked in rooms:
            # 예약할 시간이 해당 방의 마지막 예약 시각보다 크면 들어감 
            if room_booked[-1][1] <= start:
                is_reserved=True
                room_booked.append([start,end])
                break # 최소 값을 위해 다른 방 탐색x

        
        # 만약 이미 만들어진 방 중에 못들어가면 새 방 생성 및 예약
        if not is_reserved:
            rooms.append([[start,end]])
        
    # 생성한 방의 개수
    return len(rooms)

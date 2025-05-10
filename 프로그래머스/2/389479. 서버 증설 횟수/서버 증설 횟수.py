'''
1. 같은 시간대의 사람이 m명 늘어날 때마다 서버 1대가 필요함.
2. nxm<= 이용자 수  <(n+1)xm => n대가 필요함
3. 한번 증설한 서버는 K시간 동안 운영하고 그 이후는 반납해야 함.
<문제>
1. 하루동안 모든 게임 이용자가 게임을 하기 위해 서버를 최소 몇 번 증설해야하는지
2. 같은 시간대에 서버를 X대 증설했다면, 해당 시간대의 증설 횟수는 X회


<풀이>
1. 0~24까지 시간대별 시뮬레이션 시행
2. 각 시간대마다 체크 
2.1. 서버 딕셔너리에서 제거 해야하는가?
2.1.1. 현재 시각(idx)이 종료시각이랑 같음 => 서버 개수 -1 (server_cnt-1)

2.2. 현재 플레이어 몇명인가? (p: player[i])
2.2.1. 만약 지금 서버로 감당 가능한가? (rs=p//m: 필요 서버수, server_cnt < rs)
2.2.2. 불가능 => 서버 증설(서버 딕셔너리 추가 => {time=idx}:종료 시각(idx+k), server_cnt+1)
2.2.3. 가능 => 패스


'''
def solution(players, m, k):
    answer = 0
    
    server=dict() # 서버 딕셔너리
    server_cnt=0 # 서버 개수
    
    for i in range(24):
        p=players[i]
        rs=p//m
        
        # 1. 서버 정보 갱신
        remove_keys=[]
        for key,v in server.items(): 
            end_t, running_cnt=v[0],v[1]
            if i==end_t:
                server_cnt-=running_cnt
                remove_keys.append(key)
                
        # 필요없는 서버 제거
        for key in remove_keys:
            del server[key]
        
        # 2. 필요한 서버수보다 작으면 서버 증설
        if server_cnt<rs:
            add_server_cnt=rs-server_cnt
            answer+= add_server_cnt
            server_cnt+=add_server_cnt
            server[i]=[i+k,add_server_cnt] # 종료 시각, 가용 대수 설정(증설된 서버의) 
        
#         print(i,"시각의 서버 정보")
#         print("운용 서버 개수:",server_cnt)
#         print("서버 기록:",server)
#         print("정답:", answer)
#         print()
    
    return answer
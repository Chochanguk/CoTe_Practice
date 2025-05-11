def make_sec(t):
    mini=int(t[:2])
    sec=int(t[3:])
    
#     print("분:",mini)
#     print("초:",sec)
    
    return mini*60+sec
  
def make_min(seconds):
    
    mini=str(seconds//60).rjust(2,'0')
    sec=str(seconds%60).rjust(2,'0')
    
#     print("분:",mini)
#     print("초:",sec)
    
    return mini+":"+sec
    
    

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    '''
    1. prev => 10초 이전
    2. next => 10초 이후
    3. 오프닝 건너뛰기  => pos=op_end 
    
    '''
    # 모든 시간을 초로 변환
    video_len=make_sec(video_len)
    pos=make_sec(pos)
    op_start=make_sec(op_start)
    op_end	=make_sec(op_end)
    
    for command in commands:

        if op_start<=pos<=op_end:
            pos=op_end
        
        if command=='prev':
            pos=max(pos-10,0)
        if command=='next':
            pos=min(pos+10, video_len)
            
        if op_start<=pos<=op_end:
            pos=op_end
            
        # print("pos: ",make_min(pos))
    return make_min(pos)
def solution(n, lost, reserve):
    answer = 0
    
    clothes=[1]*n #모두 1개씩
    for i in reserve:
        clothes[i-1]+=1
    
    for i in lost:
        clothes[i-1]-=1
        
    print(clothes) # 기존(1)+여벌(1)-도난(1) 연산 후
# 메인 서비스
    idx=0
    while idx<n:
        if clothes[idx]==0 :
            
            # 뒤 학생에게 빌리기(최대한 많이 빌려주기 위해서)
            # 만약 앞에서 먼저 빌려주면, 뒤에 여분이 있어도 못빌려줌
            if idx >0 and clothes[idx-1]==2:
                clothes[idx]+=1
                clothes[idx-1]-=1
            # 앞 학생에게 빌리기
            elif idx < n-1 and clothes[idx+1]==2:
                clothes[idx]+=1
                clothes[idx+1]-=1
                
        idx+=1 # 다음 옷 체크
    
    # 체육복 있는 학생 수 세기
    for c in clothes:
        if c >= 1:
            answer += 1
    
    return answer
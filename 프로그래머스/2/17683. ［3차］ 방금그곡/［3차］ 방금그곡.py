'''
기억한 멜로디를 재생 시간과 제공된 악보를 직접 보며 비교
1. 몇분 재생됐는지: pt
2. pt만큼 재생해서 음을 만듦
3. 해당 음이 있는지 확인 => corrects 배열에 넣기
=> corrects=[[title,len(pt),index(순서),]..]
4. corrects -x[1], x[2] 순으로 정렬
5. 있으면 corrects[0] 반환

'''

def is_sublist(small, big):
    l = len(small)
    for i in range(len(big) - l + 1):
        if big[i:i+l] == small:
            return True
    return False

def solution(m, musicinfos):
    answer = ''
    corrects=[]
    
    # m 리스트로 변환
    m_list=[]
    for j, ch in enumerate(m):
        melody=''
        if ch=='#':
            m_list.pop() # 맨 마지막 제거
            melody=m[j-1]+'#' # 삽입
            m_list.append(melody)
        else:
            m_list.append(ch)

    # print("m_list:",m_list)

    
    for i, musicinfo in enumerate(musicinfos):
        
        s,e,title,melodys_str=musicinfo.split(",")
        
        # 시각 구하기(pt)
        sh,sm=s.split(':')
        eh,em=e.split(':')
        sh,sm=int(sh), int(sm)
        eh,em=int(eh), int(em)
        pt=(eh-sh)*60+ (em-sm)
        
        # 음 구하기
        melodys=[]
        for j,ch in enumerate(melodys_str):
            melody=''
            if ch=='#':
                melodys.pop() # 맨 마지막 제거
                melody=melodys_str[j-1]+'#' # 삽입
                melodys.append(melody)
            else:
                melodys.append(ch)
        new_melodys=[]
        l_melodys=len(melodys) # 음 길이
        # 더 짧으면
        if pt <= l_melodys:
            new_melodys=melodys[:pt+1]
        # 더 길면
        else:
            rnd=pt//l_melodys
            left=pt%l_melodys
            new_melodys=melodys*rnd + melodys[:left+1]
        # print("재생된 음:",new_melodys)
        
        if is_sublist(m_list, new_melodys):
            corrects.append([title, pt, i])
    # 기준에 정렬
    corrects.sort(key=lambda x: (-x[1], x[2]))
        
    if not corrects:
        answer='(None)'
    else:
        answer=corrects[0][0]
        
    return answer
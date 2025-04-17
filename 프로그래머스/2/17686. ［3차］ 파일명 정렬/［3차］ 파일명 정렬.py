def solution(files):
    answer = []
    '''
    [[대문자 HEAD, int(NUMBER), TAIL, 원 순서, 원본],[]]
    '''
    new_arrs=[]
    
    for idx,file in enumerate(files):
        se, ne = None, None
        for i,ch in enumerate(file):
            # 이전께 숫자가 아니고 지금이 숫자면
            if ch.isdigit() and se is None:
                se = i - 1
            # 문자열 종료가 나왔고, 아직 문자이면
            if se is not None and not ch.isnumeric():
                ne = i - 1
                break  # 숫자 다음 문자가 나왔으면 끝
                
            
        # 숫자가 마지막까지 간 경우 보정
        if ne is None:
            ne = len(file) - 1  # 숫자가 끝까지 간 경우
        # 숫자 인데스랑 5개 이상이면 se+5
        if ne-se>5:
            ne=se+5
        # head=[ ch.upper() for ch in file[i:se+1]] # 대문자임.
        # print('se: ',se)
        # print('ne: ',ne)
        # print()
        head= file[:se+1].upper() # 대문자임. 
        number=int(file[se+1:ne+1]) # 숫자로 변환
        tail=file[ne+1:]
        new_arrs.append([head,number,tail,idx,file])
    new_arrs.sort(key=lambda x: (x[0],x[1],x[3]))
    # print(new_arrs)     
    return [str_arr[4] for str_arr in new_arrs ]
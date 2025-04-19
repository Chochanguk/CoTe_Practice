def solution(record):
    answer = []
    '''
    1. 채팅방 리스트를 만듦, [(아이디, 닉네임, 상태(들어옴/나감)),  ]
    2. 아이디: [닉네임, 상태]
    '''
    result=[]
    id_dict={}
    state_dict={'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}
    for r in record:
        state,uid,nickname='','',''
        rec=r.split(' ')
        if len(rec)==3:
            state,uid,nickname=rec
        elif len(rec)==2:
            state,uid=rec
        
        # print(state,uid,nickname)
        # 만약 
        if uid not in id_dict:
            id_dict[uid]=nickname
        else:
            # 딕셔너리에 있고, 상태가 변경이면 닉네임 변경
            # 만약 상태가 들어왔고, 기존이랑 값이 다르면 변경
            if state=='Change' or ( state=='Enter' and id_dict[uid]!=nickname):
                id_dict[uid]=nickname
                
        # 닉넴 변경이 아닌 경우에는 집어 넣음
        if state != 'Change':    
            result.append((uid,state))
    # print()
    # print(id_dict)
    # print(result)
    for uid,state in result:
        output=id_dict[uid]+state_dict[state]
        answer.append(output)
    
    
    return answer
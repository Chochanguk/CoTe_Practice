def solution(msg):
    answer = []
    
    dictionary=dict() # 딕셔너리
    for i in range(ord('A'),ord('Z')+1):
        dictionary[chr(i)]=i-64
    # print(dictionary)
    
    
    last_n=len(dictionary)
    w=msg[0]
    
    for ch in msg[1:]:
        # 만약 입력값이 사전에 있으면
        if w in dictionary:
            if w+ch not in dictionary:
                answer.append(dictionary[w])
                last_n+=1
                dictionary[w+ch]=last_n
                w=ch
            else:
                w+=ch
        # 입력이 사전에 없으면 입력에 추가
        else:   
            w+=ch
    if w:
        answer.append(dictionary[w])
    
    return answer

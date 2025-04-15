def solution(s):
    # 스택
    answer = []
    tuple_list=[]
    s=s[1:-1]
    n=len(s)
    i=0
    while i<n:
        # 괄호 열리면
        if s[i]=='{':
            stack=[]
            while s[i]!='}':
                i+=1
                # 닫는 것도 아니고, 쉼표도 아니면 집어 넣음
                if s[i]!='}':
                    stack.append(s[i])
            tuple_list.append(''.join(stack).split(','))
        else:
            i+=1
    
    tuple_list.sort(key=len)
    # print()    
    # print(tuple_list)
    
    for tup in tuple_list:
        for t in tup:
            if int(t) not in answer:
                answer.append(int(t))
        
    
    return answer
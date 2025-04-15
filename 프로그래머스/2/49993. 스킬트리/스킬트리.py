def solution(skill, skill_trees):
    answer = 0
    s_dict={}
    rank=0
    for i,s in enumerate(skill):
        s_dict[s]=i
    # print(s_dict)
    for tree in skill_trees:
        tree=list(tree)
        t_list=[]
        is_ok=True
        for s in tree:
            # 만약 딕셔너리에 있으면
            if s in s_dict:
                t_list.append(s_dict[s])

        # print(t_list)
        # 빈 트리일 수 있으니
        if not t_list:
            answer+=1
            continue
            
        # 순서대로 되어 있는지 체크 (0부터 시작해서 1씩 증가해야 함,중복x)
        for i in range(len(t_list)):
            if t_list[i] != i:
                is_ok = False
                break
        
        if is_ok:
            answer+=1

    return answer
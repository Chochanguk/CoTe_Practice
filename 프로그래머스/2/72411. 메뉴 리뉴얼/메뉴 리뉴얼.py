# 1.
def get_combis(arr,r):
    result=[]
    '''
    사전순으로 넣음 => 문제에서 각 코스는 이미 오름차순으로 정렬되어있음
    [[A,B],[B,C],[A,C],]
    '''
    # 재귀 사용
    def combi(path,idx):
        # 종료 조건(스택에 개수 채우면 종료)
        if len(path)==r:
            result.append(path)
            return
        for i in range(idx,len(arr)):
            combi(path+[arr[i]],i+1)
    combi([],0)

    return result

def solution(orders, course):
    answer = []
    '''
    1. course 에서 하나씩 꺼내서(개수)만큼 한 사람당 주문 가능한 조합을 만듦
    2. 가능한 조합의 개수를 세서 딕셔너리에 넣음
    3. 최대 등장 횟수를 셈 
    4. 가장 많이 주문했던 것들을 셈 (2번 이상)
    '''
    # arr=['A','B','C']
    # print(get_combis(arr,2))
    for c in course:
        # 개수 딕셔너리
        combi_dict={}
        for order in orders:
            sorted_order=sorted(order)
            combis=get_combis(sorted_order,c)
            # print("combis:", combis)
            # 조합을 하나씩 꺼내서 딕셔너리에 넣기
            for combi in combis:
                str_combi = ''.join(combi)
                # print(str_combi)
                if str_combi not in combi_dict:
                    combi_dict[str_combi]=1
                else:
                    combi_dict[str_combi]+=1
            # print()
            # print("combi_dict:", combi_dict)
            # print()
            
        # 각 조합에서 최대개수 찾기
        max_count=-1
        for v in combi_dict.values():
            if v>=2:
                max_count=max(max_count,v)

        # 가장 많이 주문된 조합만 추가
        for k,v in combi_dict.items():
            if v==max_count and v>=2:
                answer.append(k)

    return sorted(answer) # 오름차순 정렬 후 반환
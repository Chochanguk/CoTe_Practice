def solution(sequence, k):
    n = len(sequence)
    left,right = 0,0
    total = sequence[0]
    answer = []

    min_len = float('inf')
    
    '''
    슬라이딩 윈도우 방식을 활용해 total이 K가될때까지 탐색한다.
    k가 되면 최소 길이 설정하고, 다음 탐색시 이보다 더 짧으면
    answer의 값을 갱신한다.
    
    '''   
    while right<n:
        # 만약 현재 합산이 k와 같다면
        if total==k:
            # 만약 길이가 더 짤다면
            if (right-left) < min_len:
                min_len=right-left
                answer=[left,right]
            total-=sequence[left]
            left+=1
        elif total<k:
            right+=1
            if right <n:
                total+=sequence[right]

        elif total>k:
            total-=sequence[left]
            left+=1
            
    
    return answer
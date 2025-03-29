import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) # 힙으로 바로 만듦(0(N))
    
    # 힙은 왼쪽부터 pop되며, 맨 앞은 항상 가장 작은 값이다.
    while len(scoville)>=2 and scoville[0]<K:
        first=heapq.heappop(scoville)
        second=heapq.heappop(scoville)
        
        new=first+(second*2)
        heapq.heappush(scoville, new)
        # print(scoville)
        answer+=1
    
    # 마지막 음식도 확인
    if scoville and scoville[0] < K:
        return -1
        
    return answer

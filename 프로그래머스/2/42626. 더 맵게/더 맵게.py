import heapq as hq # 별칭으로 간단하게

def solution(scoville, K):
    answer = 0
    
    hq.heapify(scoville) # 힙으로 바로 만듦(0(N))
    
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

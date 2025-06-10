'''
준호는 병사 n명을 가짐
매 라운드마다 enemy[i] 마리 적이 등장
1. 남은 병사중 enemy[i]만큼 소모하여 막음
ex) 병사 7명, 적2 명 -> 남은 병사 5명(병사 수가 음수가 되면 종료 )
2. 무적권 킬 -> 병사 소모없이 막을 수 있음.. 최대 K번
3. 최대한 많이 라운드를 진행 시키는 법은?

풀이법
0. 지금까지 나온 적 중 큰 값들은 병사를 물리치지 말자-> 무적권 사용
1. 힙에 병사를 집어 넣음.
2. 적의 수가 k개 초과시 가장 작은 값을 빼서 병사를 물리침
3. 병사가 사라지면 종료

'''

import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        # 무적권을 아직 다 쓰지 않았다면 그냥 넘김
        if len(heap) > k:
            # 가장 작은 적을 병사로 처리
            n -= heapq.heappop(heap)
        # 병사가 부족하면 종료
        if n < 0:
            return i
    
    return len(enemy)

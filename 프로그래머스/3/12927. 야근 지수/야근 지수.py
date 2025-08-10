import heapq

'''
야근 피로도 문제

- 야근 피로도 정의: 야근을 시작한 시점에서 남은 각 일의 작업량 제곱의 합
- 남은 N시간 동안 작업량을 줄여 피로도를 최소화
- 규칙: 1시간에 작업량을 1 줄일 수 있다고 가정(가장 큰 작업부터 줄이는 게 최적)

접근:
1) 총 작업량이 N 이하이면 전부 처리 가능하므로 피로도 0
2) 그 외엔 "가장 큰 작업량"을 매 시간 1씩 줄이는 것이 최적 -> 최대 힙 사용
   - 파이썬 heapq는 최소 힙이므로 음수로 변환해 저장
복잡도:
- N번 pop/push: O(N log M), M = works 길이
'''

def solution(n, works):
    total = sum(works)
    if total <= n:
        return 0

    # 최대 힙 구성(음수로 저장)
    heap = [-w for w in works if w > 0] # [2 1 2] =>[-2 -2 -1]
    heapq.heapify(heap)

    # N시간 동안 가장 큰 작업을 1씩 줄이기
    for _ in range(n):
        # 항상 가장 큰 작업을 꺼낸다
        largest = -heapq.heappop(heap)
        largest -= 1  # 1만큼 처리
        heapq.heappush(heap, -largest)

    # 남은 작업량 제곱 합(음수를 다시 양수로 돌려서 계산)
    return sum(((-x) ** 2) for x in heap)

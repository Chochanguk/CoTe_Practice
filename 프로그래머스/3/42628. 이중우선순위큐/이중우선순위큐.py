import heapq as hq

def max_heap(max_l):
    max_heap=[]
    for n in max_l:
        hq.heappush(max_heap,-int(n))
        
    return [-i for i in max_heap]

def solution(operations):
    prio_q = []

    for op in operations:
        command, num = op.split()
        num = int(num)

        if command == "I":
            hq.heappush(prio_q, num)
        elif command == "D" and prio_q:
            if num == 1:
                # 최대값 삭제
                prio_q=max_heap(prio_q)[1:]
                hq.heapify(prio_q)
            elif num == -1:
                # 최소값 삭제
                hq.heappop(prio_q)

    if prio_q:
        return [max(prio_q), min(prio_q)]
    else:
        return [0, 0]

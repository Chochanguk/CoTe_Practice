import heapq as hq

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
                max_val = max(prio_q)
                prio_q.remove(max_val)
                hq.heapify(prio_q)
            elif num == -1:
                # 최소값 삭제
                hq.heappop(prio_q)

    if prio_q:
        return [max(prio_q), min(prio_q)]
    else:
        return [0, 0]

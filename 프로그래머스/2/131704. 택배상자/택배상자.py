from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    container = [i for i in range(1, n+1)]
    stack = []
    idx = 0  # order의 인덱스
    
    for box in container:
        stack.append(box)
        
        # 스택의 top이 order[idx]와 같을 경우 계속 pop
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
            answer += 1
            if idx == n:
                break
                
    return answer

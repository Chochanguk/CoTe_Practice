def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 가격이 떨어진 경우 계산
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    # 끝까지 떨어지지 않은 것 처리
    while stack:
        prev = stack.pop()
        answer[prev] = n - 1 - prev

    return answer

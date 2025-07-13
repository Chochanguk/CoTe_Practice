def solution(k, d):
    answer = 0
    d_squared = d * d

    for x in range(0,d+1,k): # x: 0 ~ d 
        # x 고정일 때 가능한 최대 y 값 찾기
        # x^2 + y^2 <= d^2 → y^2 <= d^2 - x^2
        max_y= (d_squared - x * x)**0.5 # y의 최대 범위

        # y는 0, k, 2k, ..., max_y 이하까지
        count = (max_y // k) + 1
        answer += count

        x = k # 다음 x 찾기

    return answer

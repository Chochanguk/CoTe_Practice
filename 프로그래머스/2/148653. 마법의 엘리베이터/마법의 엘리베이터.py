'''
0보다 작으면 엘리베이터는 움직이지 않음
0층이 가장 아래층, 현재 엘리베이터 민수 위치
-1, +1 , -10, +10, -100, +100 ...

버튼 누른


0~4 => -
5~9 => +

'''

def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    
    carry = 0
    for i in range(len(storey)-1, -1, -1):
        cur = storey[i] + carry

        if cur > 5:
            answer += 10 - cur
            carry = True
        elif cur < 5:
            answer += cur
            carry = False
        else:  # cur == 5
            '''
            다음 자리수가 5 이상이면 올리는 게 유리
            
            ex) 95 -> 90 (5번) -> 0(9번)
                95 -> 100(5번) -> 0(10번)
            '''
            if i > 0 and storey[i-1] >= 5:
                answer += 10 - cur
                carry = True
            else:
                answer += cur
                carry = False

    if carry:
        answer += 1

    return answer


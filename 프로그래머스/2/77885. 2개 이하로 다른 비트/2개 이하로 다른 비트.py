def solution(numbers):
    answer = []

    for number in numbers:
        # 짝수면 그 다음 수가 정답임
        if number % 2 == 0:
            answer.append(number + 1)
        # 홀수면
        # 오른쪽에서 처음 나오는 0을 1로 바꾸고, 바로 뒤 비트는 0으로 바꾸면 만족
        else:
    
            bit = '0' + bin(number)[2:]  # 앞에 '0' 붙여서 2진수 문자열로 변환
            idx = bit.rfind('0')  # 가장 오른쪽 0 찾기
            bit = list(bit) # 리스트로 변환하여 요소 접근
            bit[idx] = '1'
            bit[idx + 1] = '0'
            answer.append(int(''.join(bit), 2)) # 해당 비트를 10진수로 변환 후 추가
    
    return answer
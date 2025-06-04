import math
    
def solution(n, k):
    nums = list(range(1, n + 1)) # 1~n 까지의 수
    k -= 1  # 0번째 인덱스 맞춤
    answer = []
    print("nums: ",nums)

    while n > 0:
        '''
        (n-1)! => 고정된 자리수 다음의 경우의 수
        ex: 1 => (2,3), (3,2) => 2개의 묶음
        
        1. 몇 번째 숫자를 골라야 하는지 계산
         ex: 3,1,2 에서 3을 고르려면 앞에서 4번 수행([1, 2, 3],[1, 3, 2],[2, 1, 3], [2, 3, 1]) 후
         그 다음 묶음 선택
         
        2. 골라낸 숫자는 리스트에서 제거

        3. 남은 숫자들로 다시 반복
        '''
        n -= 1
        fact = math.factorial(n) 
        
        # 지금 몇 번째 묶음인지
        index = k // fact
        
        # 해당 인덱스 뽑고, 그 숫자는 사용 안함.
        answer.append(nums.pop(index))
        
        # 현재 그룹에서 몇 번째 위치인지를 업데이트
        k %= fact

    return answer

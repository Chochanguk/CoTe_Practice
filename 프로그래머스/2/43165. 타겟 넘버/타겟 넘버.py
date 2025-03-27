operators_list =[] # 연산자의 모든 경우를 담은 리스트 -> 전역 변수?

# n은 채우질 개수, 현재 깊이
def back_tracking(n,depth, operators):
    # 백트래킹 종료 조건(depth가 n에 도달)
    if depth==n:
        operators_list.append(operators)
        return 
    
    back_tracking(n, depth+1, operators+["+"])
    back_tracking(n, depth+1, operators+["-"])


# 연산자와 numbers의 합을 구하는 함수
def cal(operators, numbers):
    result=0
    for op, num in zip(operators, numbers):
        if op=="+":
            result+=num
        else:
            result-=num
    return result
    
    

def solution(numbers, target):
    answer = 0
    '''
    1. 모든 경우 탐색 => 2. 백트래킹 
    3. 백트래킹의 요소 => +, - 추가하고 빼기
    4. stack(4개)가 다 쌓이면 종료~
    5. 가능한 연산자 조합의 리스트를 반환 (리스트를 입력)
    6. 그 연산자 리스트를 하나씩 꺼내어 리스트의 값에 대입하여
    target이 되는 순간 answer 증가
    
    []4 []1 []2 []1
    
    [[+,+,+,+],[+,+,+,-]....[-,-,-,-]]

    '''
    n=len(numbers)
    back_tracking(n,0,[])
    # print(operators_list)
    
    for operators in operators_list:
        result=cal(operators, numbers)
        if result==target:
            answer+=1
    
    return answer
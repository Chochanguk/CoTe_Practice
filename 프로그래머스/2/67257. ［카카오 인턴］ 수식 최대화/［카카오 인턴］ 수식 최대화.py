'''
우승자에게 상금 지급 방식 문제

1. +,-,* 연산만 주어짐
2. 연산자의 우선순위는 자유롭게 재정의 (팩토리얼 경우의 수)
3. 결과가 음수라면 절대값으로 변환하여 제출
4. 제출 숫자가 가장 큰 참가자를 우승자로 선정

ex) 100-200*300-500+20

* > + > - 
우선 순이면 -60,420 => 60,420이 돼서 최대 값이 됨.
숫자는 0 ~ 999까지임(숫자는 음수 없음)

풀이법

1. 숫자들을 모음
2. 연산자들을 모음(딕셔너리 "+": [인덱스1,인덱스2 ...])
3. +,-,* 들의 리스트를 선택하며 우선순위를 정함
operators=[['+','-','*'],['+','*','-'],...]
4. operators에서 하나씩 꺼내서 연산 

'''

# 백트래킹으로 가능한 연산자 우선순위를 만듦
def dfs(op_cnt,op_set,prior_ops):
    
    global prior_operations
    
    if len(prior_ops)==op_cnt:
        prior_operations.append(prior_ops)
        return
    
    for op in op_set:
        if op not in prior_ops:
            dfs(op_cnt,op_set,prior_ops+[op])

        
prior_operations=[]

def cal(numbers, operators, prior_operations):
    max_result = -float('inf')
    
    for ordered_ops in prior_operations:
        temp_nums = numbers[:]  # 리스트 복사
        temp_ops = operators[:]
        
        for op in ordered_ops:
            idx = 0
            while idx < len(temp_ops):
                if temp_ops[idx] == op:
                    # 해당 연산을 처리
                    if op == '+':
                        temp = temp_nums[idx] + temp_nums[idx + 1]
                    elif op == '-':
                        temp = temp_nums[idx] - temp_nums[idx + 1]
                    elif op == '*':
                        temp = temp_nums[idx] * temp_nums[idx + 1]
                    
                    # 연산 후 리스트를 수정
                    temp_nums[idx] = temp
                    del temp_nums[idx + 1]
                    del temp_ops[idx]
                else:
                    idx += 1
        
        max_result = max(max_result, abs(temp_nums[0]))  # 결과는 하나의 숫자만 남음
    
    return max_result



def solution(expression):
    answer = 0
    
    numbers=[]  # 사용된 숫자들
    operators=[] # 사용된 연산자들(순서 고려)
    op_set=set() # 사용된 연산자
    
    num=[] # 임시 숫자
    for i,ch in enumerate(expression):
        num.append(ch)
        if ch=='-':
            num.pop()
            numbers.append(int(''.join(num)))
            num=[]
            operators.append('-')      
            op_set.add('-')
        if ch=='+':
            num.pop()
            numbers.append(int(''.join(num)))
            num=[]
            operators.append('+')
            op_set.add('+')
        if ch=='*':
            num.pop()
            numbers.append(int(''.join(num)))
            num=[]
            operators.append('*')           
            op_set.add('*')
        
    numbers.append(int(''.join(num)))
    
    op_cnt=len(list(op_set))
    dfs(op_cnt,list(op_set),[]) # 연산 우선 순위
    
    # print(f'numbers {numbers}')
    # print(f'operators {operators}')
    # print(f'op_set {op_set}')
    # print(f'prior_operations {prior_operations}')
    
    answer=cal(numbers,operators,prior_operations)
    
    return answer
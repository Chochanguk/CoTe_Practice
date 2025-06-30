'''
1.  (,) 개수가 같으면 "균형 잡힌 괄호 문자열"
2. 짝도 맞으면 "올바른 괄호 문자열"
'''

from collections import deque

# 균형 -> 올바른 
def convert_to(p):
    # 1. 입력이 빈 문자열이면 빈 문자열 반환
    if not p:
        return ''
    
    u, v = '', ''
    left_cnt, right_cnt = 0, 0
    
    # 2. u, v로 분리하기
    for i, ch in enumerate(p):
        if ch == '(':
            left_cnt += 1
        else:
            right_cnt += 1
        
        if left_cnt == right_cnt:
            u=p[:i+1]
            v = p[i+1:]
            break
    
    # 3. u가 올바른 괄호 문자열이면 v를 재귀적으로 변환 후 u에 붙임
    if is_alright(u):
        return u + convert_to(v)
    # 4. 
    else:
        # u가 올바르지 않으면 다음 규칙에 따라 변환
        temp = '('
        temp += convert_to(v)
        temp += ')'
        #4.4 u의 첫, 마지막 문자 제거하고 나머지를 뒤집기
        flipped = []
        for ch in u[1:-1]:
            if ch=='(':
                flipped.append(')')
            else:
                flipped.append('(')
        temp += ''.join(flipped)
        
        return temp


# 올바른 괄호인가?
def is_alright(p):
    is_ok=False
    stack=[]
    for ch in p:
        
        if ch=="(":
            stack.append(ch)
        else:
            # 스택이 비어있는데 pop하면 False
            if not stack:
                # print("is_ok: ",is_ok)
                return False
            stack.pop()
                
    # 스택이 비어있으면 True
    if not stack:
        is_ok=True
    
    # print("is_ok: ",is_ok)
    
    return is_ok

# 균형잡힌 괄호인가?
def is_balanced(p): return p.count('(')==p.count(')')

def solution(p):
    
    # 빈 문자열일 경우 빈문자열 반환
    if not p:
        return p
    
    # 이미 올바른 괄호이면 반환
    if is_alright(p):
        return p
    
    # 균형잡힌 괄호이면 변환
    if is_balanced(p):
        p=convert_to(p)
        
    return p
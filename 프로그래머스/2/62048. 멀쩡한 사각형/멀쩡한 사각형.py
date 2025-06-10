import math

def find_cross(w,h):
    cnt=0
    
    '''
    1. w,h의 최대 공약수 구함
    2. w+-gcd= 지나가는 직사각형 수
    '''
    
    gcd=math.gcd(w,h)
    
    cnt=w+h-gcd

    return cnt

def solution(w,h):
    answer = 1
    
    neobi=w*h
    unused=0
    
    # 정사각형
    if w==h:
        unused = w
    # 직사각형
    else:
        unused = find_cross(w,h)

    return neobi-unused
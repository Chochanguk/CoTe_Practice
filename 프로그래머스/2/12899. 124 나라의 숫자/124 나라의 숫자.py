def solution(n):
    answer = ''
    result=[]

    while n > 0:
        el = n % 3
        if el==0:
            result.append(str('4'))
            n = (n-1)// 3 # 몫을 하나 더 줄임
        else:
            result.append(str(el))
            n //= 3
    
    answer=''.join(result)[::-1]
    print(answer)
    return answer

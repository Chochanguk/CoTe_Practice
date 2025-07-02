def solution(data, col, row_begin, row_end):
    answer = 0
    
    #1. col번째 기준 정렬, 첫번째 기준 내림차순
    data.sort(key=lambda x: (x[col-1],-x[0]))
    # print(data)
    
    #2. 
    result=0
    for idx in range(row_begin-1, row_end):
        mod=idx+1
        row_sum = 0
        for val in data[idx]:
            row_sum+=val%mod
        result=result^row_sum
        
    return result
'''
5+16 = 21 =10.5 (0~1)
16+8 = 24 = 12  (1~2)
8+4 =12 = 6     (2~3)
4+2 = 6 = 3     (3~4)
2+1 =3 = 1.5    (4~5)

21+24+15
45+15=66//2=33.0

문제 풀이:
각 x 좌표마다 y의 값을 미리 구해서 딕셔너리로 표기

정적분 계산



'''

def cal(sx,ex,coor_dict):
    if sx<=ex:
        result=0
        for x in range(sx+1,ex+1):
            # print(coor_dict[x])
            # print(f'결과: {result}')
            result+=(coor_dict[x-1]+coor_dict[x])
    else:
        return -1
    # print()
    # print(f'결과: {result}')
    # print()
    
    return result/2.0

def solution(k, ranges):
    answer = []

    coor_dict=dict()
    idx=0
    coor_dict[0]=k

    while k>1:
        
        if k%2==0:
            k//=2
            idx+=1
            if k>=1:
                coor_dict[idx]=k    
        else:
            k=k*3+1
            idx+=1
            coor_dict[idx]=k
    
    # print(coor_dict)
    end=idx
    for sx,ex in ranges:
        ex=end+ex
        # print(f'(sx,ex): ({sx},{ex})')
        answer.append(cal(sx,ex,coor_dict))
    return answer
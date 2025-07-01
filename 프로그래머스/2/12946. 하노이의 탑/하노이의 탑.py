'''
1. 세 개의 기둥
2. 한번에 하나의 원판만 옮김
3. 큰원판이 작은 원판 위에 있으면 안됨
4. 1->3으로 옮기기
'''
def solution(n):
    answer = []
    
    def hanoi(n,start,end,temp):
        # 옮겨야 할게 1개이면 재귀 종료
        if n == 1:
            answer.append([start, end])
            return
        
        hanoi(n-1,start,temp,end) #1. n-1개를 중간으로 옮김 
        answer.append([start, end]) # 옮긴거 추가
        hanoi(n-1,temp,end,start) #2. n-1개를 중간에서 종료로 옮김 
        
    hanoi(n,1,3,2)
    return answer